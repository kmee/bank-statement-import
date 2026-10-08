import base64

from odoo.exceptions import UserError
from odoo.tests.common import TransactionCase
from odoo.tools.misc import file_path

ACCTID = "5118005031"


class TestAcctidMatchBr(TransactionCase):
    """ACCTID matching with a clean account number (e.g. Brazilian bank)."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.asi_model = cls.env["account.statement.import"]
        cls.usd = cls.env.ref("base.USD")
        cls.partner = cls.env.ref("base.main_partner")
        cls.company = cls.env.ref("base.main_company")
        cls.journal_a = cls._create_journal("00503", ACCTID, "TBR1")
        cls.journal_other = cls._create_journal("999888", "999888-Z", "TBR2")
        path = file_path(
            "account_statement_import_ofx_by_acctid/tests/test_ofx_file/"
            "test_ofx_acctid_br.ofx"
        )
        with open(path, "rb") as f:
            cls.ofx_file = base64.b64encode(f.read())

    @classmethod
    def _create_journal(cls, acc_number, acctid, code):
        vals = {
            "acc_number": acc_number,
            "partner_id": cls.partner.id,
            "company_id": cls.company.id,
        }
        if acctid:
            vals["acctid"] = acctid
        bank = cls.env["res.partner.bank"].create(vals)
        return cls.env["account.journal"].create(
            {
                "name": f"Journal {code}",
                "code": code,
                "type": "bank",
                "bank_account_id": bank.id,
                "currency_id": cls.usd.id,
            }
        )

    def _wizard(self, journal_id=None):
        wizard = self.asi_model.create(
            {"statement_file": self.ofx_file, "statement_filename": "t.ofx"}
        )
        if journal_id:
            wizard = wizard.with_context(journal_id=journal_id)
        return wizard

    def test_match_clean_account_without_context(self):
        journal = self._wizard()._match_journal(ACCTID, self.usd)
        self.assertEqual(journal, self.journal_a)

    def test_match_clean_account_with_context(self):
        journal = self._wizard(self.journal_a.id)._match_journal(ACCTID, self.usd)
        self.assertEqual(journal, self.journal_a)

    def test_match_with_other_journal_in_context(self):
        with self.assertRaises(UserError):
            self._wizard(self.journal_other.id)._match_journal(ACCTID, self.usd)

    def test_no_acctid_match_without_context(self):
        # Core behavior: no account found -> UserError
        with self.assertRaises(UserError):
            self._wizard()._match_journal("123123123", self.usd)

    def test_no_acctid_match_with_context(self):
        # Core behavior: the journal of the context is not rejected by the
        # acctid lookup; the core then fails only because no account matches.
        wizard = self._wizard(self.journal_other.id)
        with self.assertRaises(UserError) as cm:
            wizard._match_journal("123123123", self.usd)
        self.assertNotIn("not consistent", str(cm.exception))

    def test_decoy_account_substring_collision(self):
        # Another journal whose account number contains "00503" must not be
        # picked instead of the journal matched by acctid.
        decoy = self._create_journal("1005031", None, "TBR3")
        # make the decoy sort first
        decoy.sequence = self.journal_a.sequence - 1
        journal = self._wizard()._match_journal(ACCTID, self.usd)
        self.assertEqual(journal, self.journal_a)
        self.assertNotEqual(journal, decoy)
