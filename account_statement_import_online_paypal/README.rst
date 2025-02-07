==================================
Online Bank Statements: PayPal.com
==================================

.. 
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! source digest: sha256:780f46a701603229f7c422be341139ec30036a68f94edd882522647306e0f2cc
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-OCA%2Fbank--statement--import-lightgray.png?logo=github
    :target: https://github.com/OCA/bank-statement-import/tree/14.0/account_statement_import_online_paypal
    :alt: OCA/bank-statement-import
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.odoo-community.org/projects/bank-statement-import-14-0/bank-statement-import-14-0-account_statement_import_online_paypal
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :target: https://runboat.odoo-community.org/builds?repo=OCA/bank-statement-import&target_branch=14.0
    :alt: Try me on Runboat

|badge1| |badge2| |badge3| |badge4| |badge5|

This module provides online bank statements from
`PayPal.com <https://paypal.com/>`__.

**Table of contents**

.. contents::
   :local:

Configuration
=============

To configure online bank statements provider:

#. Go to *Invoicing > Configuration > Bank Accounts*
#. Open bank account to configure and edit it
#. Set *Bank Feeds* to *Online*
#. Select *PayPal.com* as online bank statements provider in
   *Online Bank Statements (OCA)* section
#. Save the bank account
#. Click on provider and configure provider-specific settings.

or, alternatively:

#. Go to *Invoicing > Overview*
#. Open settings of the corresponding journal account
#. Switch to *Bank Account* tab
#. Set *Bank Feeds* to *Online*
#. Select *PayPal.com* as online bank statements provider in
   *Online Bank Statements (OCA)* section
#. Save the bank account
#. Click on provider and configure provider-specific settings.

To obtain *Client ID* and *Secret*:

#. Open `PayPal Developer <https://developer.paypal.com/developer/applications/>`_
#. Go to *My Apps & Credentials* and switch to *Live*
#. Under *REST API apps*, click *Create App* to create new application (e.g. *Odoo*)
#. Copy *Client ID* and *Secret* to use during provider configuration
#. Under *Live App Settings*, uncheck all features except *Transaction Search*
#. Click Save

Usage
=====

To pull historical bank statements:

#. Go to *Invoicing > Configuration > Bank Accounts*
#. Select specific bank accounts
#. Launch *Actions > Online Bank Statements Pull Wizard*
#. Configure date interval and click *Pull*

Known issues / Roadmap
======================

* Only transactions for the previous three years are retrieved, historical data
  can be imported manually, see ``account_bank_statement_import_paypal``. See
  `PayPal Help Center article <https://www.paypal.com/us/smarthelp/article/why-can't-i-access-transaction-history-greater-than-3-years-ts2241>`_
  for details.
* `PayPal Transaction Info <https://developer.paypal.com/docs/api/sync/v1/#definition-transaction_info>`_
  defines extra fields like ``tip_amount``, ``shipping_amount``, etc. that
  could be useful to be decomposed from a single transaction.
* There's a known issue with PayPal API that on every Monday for couple of
  hours after UTC midnight it returns ``INVALID_REQUEST`` incorrectly: their
  servers have not inflated the data yet. PayPal tech support confirmed this
  behaviour in case #06650320 (private).

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/bank-statement-import/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
`feedback <https://github.com/OCA/bank-statement-import/issues/new?body=module:%20account_statement_import_online_paypal%0Aversion:%2014.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* CorporateHub

Contributors
~~~~~~~~~~~~

* `CorporateHub <https://corporatehub.eu/>`__

  * Alexey Pelykh <alexey.pelykh@corphub.eu>
* Omar Castiñeira <omar@comunitea.com>

Maintainers
~~~~~~~~~~~

This module is maintained by the OCA.

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

.. |maintainer-alexey-pelykh| image:: https://github.com/alexey-pelykh.png?size=40px
    :target: https://github.com/alexey-pelykh
    :alt: alexey-pelykh

Current `maintainer <https://odoo-community.org/page/maintainer-role>`__:

|maintainer-alexey-pelykh| 

This module is part of the `OCA/bank-statement-import <https://github.com/OCA/bank-statement-import/tree/14.0/account_statement_import_online_paypal>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
