# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| bag/templates/bag | [bag.html](https://github.com/colmwoods/PCPartsIreland/blob/main/bag/templates/bag/bag.html) | https://pcpartsireland-1cfc0205aac1.herokuapp.com/bag/ | ![screenshot](documentation/validation/html-bag.jpg) |  |
| bag/templates/bag | [bag-total.html](https://github.com/colmwoods/PCPartsIreland/blob/main/bag/templates/bag/bag-total.html) | N/A | ![screenshot](documentation/validation/html-bag.jpg) | Validated via rendered /bag/ page (partial template). |
| bag/templates/bag | [checkout-buttons.html](https://github.com/colmwoods/PCPartsIreland/blob/main/bag/templates/bag/checkout-buttons.html) | N/A | ![screenshot](documentation/validation/html-bag.jpg) | Validated via rendered /bag/ page (partial template). |
| bag/templates/bag | [product-image.html](https://github.com/colmwoods/PCPartsIreland/blob/main/bag/templates/bag/product-image.html) | N/A | ![screenshot](documentation/validation/html-bag.jpg) | Validated via rendered /bag/ page (partial template). |
| bag/templates/bag | [product-info.html](https://github.com/colmwoods/PCPartsIreland/blob/main/bag/templates/bag/product-info.html) | N/A | ![screenshot](documentation/validation/html-bag.jpg) | Validated via rendered /bag/ page (partial template). |
| bag/templates/bag | [quantity-form.html](https://github.com/colmwoods/PCPartsIreland/blob/main/bag/templates/bag/quantity-form.html) | N/A | ![screenshot](documentation/validation/html-bag.jpg) | Validated via rendered /bag/ page (partial template). |
| checkout/templates/checkout | [checkout.html](https://github.com/colmwoods/PCPartsIreland/blob/main/checkout/templates/checkout/checkout.html) | https://pcpartsireland-1cfc0205aac1.herokuapp.com/checkout | ![screenshot](documentation/validation/html-checkout.jpg) | |
| checkout/templates/checkout | [checkout_success.html](https://github.com/colmwoods/PCPartsIreland/blob/main/checkout/templates/checkout/checkout_success.html) | N/A | ![screenshot](documentation/validation/html-checkout_success.jpg) | Can't get a url page as its checkout_success followed by customers order number |
| faq/templates/faq | [faq.html](https://github.com/colmwoods/PCPartsIreland/blob/main/faq/templates/faq/faq.html) | https://pcpartsireland-1cfc0205aac1.herokuapp.com/faq/ | ![screenshot](documentation/validation/html-faq.jpg) | |
| form/templates/form | [contact.html](https://github.com/colmwoods/PCPartsIreland/blob/main/form/templates/form/contact.html) | https://pcpartsireland-1cfc0205aac1.herokuapp.com/contact/ | ![screenshot](documentation/validation/html-contact.jpg) ||
| form/templates/form | [return_form.html](https://github.com/colmwoods/PCPartsIreland/blob/main/form/templates/form/return_form.html) | https://pcpartsireland-1cfc0205aac1.herokuapp.com/returns/ | ![screenshot](documentation/validation/html-return_form.jpg) |  |
| form/templates/form | [return_success.html](https://github.com/colmwoods/PCPartsIreland/blob/main/form/templates/form/return_success.html) | https://pcpartsireland-1cfc0205aac1.herokuapp.com/returns/success/ | ![screenshot](documentation/validation/html-return_success.jpg) | |
| form/templates/form | [success.html](https://github.com/colmwoods/PCPartsIreland/blob/main/form/templates/form/success.html) | https://pcpartsireland-1cfc0205aac1.herokuapp.com/success/ | ![screenshot](documentation/validation/html-success.jpg) | |
| home/templates/home | [index.html](https://github.com/colmwoods/PCPartsIreland/blob/main/home/templates/home/index.html) | https://pcpartsireland-1cfc0205aac1.herokuapp.com/ | ![screenshot](documentation/validation/html-index.jpg) | |
| home/templates/home | [about.html](https://github.com/colmwoods/PCPartsIreland/blob/main/home/templates/home/about.html) | https://pcpartsireland-1cfc0205aac1.herokuapp.com/about/ | ![screenshot](documentation/validation/html-about.jpg) | |
| products/templates/products | [add_product.html](https://github.com/colmwoods/PCPartsIreland/blob/main/products/templates/products/add_product.html) | https://www.pcpartsireland.com/products/add/ | ![screenshot](documentation/validation/html-add_product.jpg) | Only superusers / admin can access this page to add products |
| products/templates/products | [edit_product.html](https://github.com/colmwoods/PCPartsIreland/blob/main/products/templates/products/edit_product.html) | https://www.pcpartsireland.com/products/3/edit/ | ![screenshot](documentation/validation/html-edit_product.jpg) | Link is for a specific product (gtx 1060). Only superusers / admin can access this page to edit products |
| products/templates/products | [product_detail.html](https://github.com/colmwoods/PCPartsIreland/blob/main/products/templates/products/product_detail.html) | https://www.pcpartsireland.com/products/3/edit/ | ![screenshot](documentation/validation/html-product_detail.jpg) | Link is for a specific product (gtx 1060). |
| products/templates/products | [products.html](https://github.com/colmwoods/PCPartsIreland/blob/main/products/templates/products/products.html) | https://pcpartsireland-1cfc0205aac1.herokuapp.com/products/ | ![screenshot](documentation/validation/html-products.jpg) | |
| products/templates/search | [search_results.html](https://github.com/colmwoods/PCPartsIreland/blob/main/products/templates/search/search_results.html) | https://www.pcpartsireland.com/products/search/?q=ryzen | ![screenshot](documentation/validation/html-search_results.jpg) | Used the word ryzen, and searched |
| products/templates/products/custom_widget_templates | [custom_clearable_file_input.html](https://github.com/colmwoods/PCPartsIreland/blob/main/products/templates/products/custom_widget_templates/custom_clearable_file_input.html) | N/A | ![screenshot](documentation/validation/html-products.jpg) | Validated via rendered /products/add page (partial template). |
| products/templates/products/includes | [quantity_input_script.html](https://github.com/colmwoods/PCPartsIreland/blob/main/products/templates/products/includes/quantity_input_script.html) | N/A | ![screenshot](documentation/validation/html-products.jpg) | Validated via rendered /products/add page (partial template). |
| profiles/templates/profiles | [confirm_delete_profile.html](https://github.com/colmwoods/PCPartsIreland/blob/main/profiles/templates/profiles/confirm_delete_profile.html) | https://www.pcpartsireland.com/profile/delete/confirm/ | ![screenshot](documentation/validation/html-confirm_delete_profile.jpg) | Customer has to be logged in to access this page |
| profiles/templates/profiles | [profile.html](https://github.com/colmwoods/PCPartsIreland/blob/main/profiles/templates/profiles/profile.html) | https://www.pcpartsireland.com/profile/ | ![screenshot](documentation/validation/html-profile.jpg) | Customer has to be logged in to access this page |
| templates | [base.html](https://github.com/colmwoods/PCPartsIreland/blob/main/templates/base.html) | https://www.pcpartsireland.com/ | ![screenshot](documentation/validation/html-index.jpg) | Validated via rendered pages extending base.html (e.g. homepage) |
| templates | [404.html](https://github.com/colmwoods/PCPartsIreland/blob/main/templates/404.html) | https://www.pcpartsireland.com/404 | ![screenshot](documentation/validation/html-404.jpg) | |
| templates | [500.html](https://github.com/colmwoods/PCPartsIreland/blob/main/templates/500.html) | N/A | ![screenshot](documentation/validation/html-500.jpg) | 500 error page validated by triggering a temporary server exception. |
| templates/includes | [main-nav.html](https://github.com/colmwoods/PCPartsIreland/blob/main/templates/includes/main-nav.html) | https://www.pcpartsireland.com/ | ![screenshot](documentation/validation/html-index.jpg) | Validated via the rendered homepage where main-nav.html is included through base.html. |
| templates/includes | [top-header.html](https://github.com/colmwoods/PCPartsIreland/blob/main/templates/includes/top-header.html) | https://www.pcpartsireland.com/ | ![screenshot](documentation/validation/html-index.jpg) | Validated via the rendered homepage where main-nav.html is included through base.html. |
| templates/includes/toasts | [toast_error.html](https://github.com/colmwoods/PCPartsIreland/blob/main/templates/includes/toasts/toast_error.html) | https://www.pcpartsireland.com/products/add/ | ![screenshot](documentation/validation/html-add_product.jpg) | Validated via rendered error toast displayed on the product add page when a form validation error occurs. |
| templates/includes/toasts | [toast_info.html](https://github.com/colmwoods/PCPartsIreland/blob/main/templates/includes/toasts/toast_info.html) | N/A | ![screenshot](documentation/validation/html-checkout_success.jpg) | Validated via informational toast displayed when viewing a past order confirmation in the user profile order history (requires logged-in user with existing order). |
| templates/includes/toasts | [toast_success.html](https://github.com/colmwoods/PCPartsIreland/blob/main/templates/includes/toasts/toast_success.html) | https://www.pcpartsireland.com/products/add/ | ![screenshot](documentation/validation/html-add_product.jpg) | Validated via rendered success toast displayed after successfully adding a product. |
| templates/includes/toasts | [toast_warning.html](https://github.com/colmwoods/PCPartsIreland/blob/main/templates/includes/toasts/toast_warning.html) | https://www.pcpartsireland.com/accounts/signup/ | ![screenshot](documentation/validation/html-signup.jpg) | Validated via rendered warning toast displayed when password validation fails during account registration. |
| templates/account | [base.html](https://github.com/colmwoods/PCPartsIreland/blob/main/templates/account/base.html) | https://www.pcpartsireland.com/accounts/login/ | ![screenshot](documentation/validation/html-login.jpg) | Validated via rendered login page extending account/base.html within the Django Allauth authentication templates. |
| templates/account | [login.html](https://github.com/colmwoods/PCPartsIreland/blob/main/templates/account/login.html) | https://pcpartsireland-1cfc0205aac1.herokuapp.com/accounts/login/ | ![screenshot](documentation/validation/html-login.jpg) | |
| templates/account | [logout.html](https://github.com/colmwoods/PCPartsIreland/blob/main/templates/account/logout.html) | https://www.pcpartsireland.com/accounts/logout/ | ![screenshot](documentation/validation/html-logout.jpg) | Only accessible to people that are logged in |
| templates/account | [password_reset.html](https://github.com/colmwoods/PCPartsIreland/blob/main/templates/account/password_reset.html) | https://www.pcpartsireland.com/accounts/password/reset/ | ![screenshot](documentation/validation/html-password_reset.jpg) | Validated via rendered password reset request page where users submit their email to receive a password reset link. |
| templates/account | [password_reset_done.html](https://github.com/colmwoods/PCPartsIreland/blob/main/templates/account/password_reset_done.html) | https://www.pcpartsireland.com/accounts/password/reset/done/ | ![screenshot](documentation/validation/html-password_reset_done.jpg) | Validated via rendered confirmation page displayed after submitting a password reset request. |
| templates/account | [password_reset_from_key.html](https://github.com/colmwoods/PCPartsIreland/blob/main/templates/account/password_reset_from_key.html) | https://www.pcpartsireland.com/accounts/password/reset/key/2-set-password/ | ![screenshot](documentation/validation/html-password_reset_from_key.jpg) | Validated via password reset form accessed through the secure reset link sent to the user's email. |
| templates/account | [password_reset_from_key_done.html](https://github.com/colmwoods/PCPartsIreland/blob/main/templates/account/password_reset_from_key_done.html) | https://www.pcpartsireland.com/accounts/password/reset/done/ | ![screenshot](documentation/validation/html-password_reset_from_key_done.jpg) | Validated via confirmation page displayed after successfully resetting the account password. |
| templates/account | [signup.html](https://github.com/colmwoods/PCPartsIreland/blob/main/templates/account/signup.html) | https://pcpartsireland-1cfc0205aac1.herokuapp.com/accounts/signup/ | ![screenshot](documentation/validation/html-signup.jpg) | |

**Note:**  
The currency selection routes (EUR, USD, GBP) are rendered dynamically via Django views and do not correspond to standalone template files. These routes were validated using the deployed URL and passed W3C validation.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| dynamic view | EUR (set_currency) | https://pcpartsireland-1cfc0205aac1.herokuapp.com/set-currency/EUR/ | ![screenshot](documentation/validation/html-eur.jpg) | Rendered via Django view |
| dynamic view | USD (set_currency) | https://pcpartsireland-1cfc0205aac1.herokuapp.com/set-currency/USD/ | ![screenshot](documentation/validation/html-usd.jpg) | Rendered via Django view |
| dynamic view | GBP (set_currency) | https://pcpartsireland-1cfc0205aac1.herokuapp.com/set-currency/GBP/ | ![screenshot](documentation/validation/html-gbp.jpg) | Rendered via Django view |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| checkout/static/checkout/css | [checkout.css](https://github.com/colmwoods/PCPartsIreland/blob/main/checkout/static/checkout/css/checkout.css) | N/A | ![screenshot](documentation/validation/css-checkout.jpg) | |
| home/static/home/css | [home.css](https://github.com/colmwoods/PCPartsIreland/blob/main/home/static/home/css/home.css) | N/A | ![screenshot](documentation/validation/css-home.jpg) | |
| profiles/static/profiles/css | [profile.css](https://github.com/colmwoods/PCPartsIreland/blob/main/profiles/static/profiles/css/profile.css) | N/A | ![screenshot](documentation/validation/css-profile.jpg) | |
| static/css | [base.css](https://github.com/colmwoods/PCPartsIreland/blob/main/static/css/base.css) | N/A | ![screenshot](documentation/validation/css-static-base.jpg) | |

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| checkout/static/checkout/js | [stripe_elements.js](https://github.com/colmwoods/PCPartsIreland/blob/main/checkout/static/checkout/js/stripe_elements.js) | N/A | ![screenshot](documentation/validation/js-checkout-stripe_elements.jpg) | Used /* jshint esversion: 11, jquery: true */ /* global Stripe */ up top of file |

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| . | [custom_storages.py](https://github.com/colmwoods/PCPartsIreland/blob/main/custom_storages.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/custom_storages.py) | ![screenshot](documentation/validation/py--custom_storages.jpg) | |
| . | [manage.py](https://github.com/colmwoods/PCPartsIreland/blob/main/manage.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/manage.py) | ![screenshot](documentation/validation/py--manage.jpg) | |
| bag | [admin.py](https://github.com/colmwoods/PCPartsIreland/blob/main/bag/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/bag/admin.py) | ![screenshot](documentation/validation/py-bag-admin.jpg) | |
| bag | [apps.py](https://github.com/colmwoods/PCPartsIreland/blob/main/bag/apps.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/bag/apps.py) | ![screenshot](documentation/validation/py-bag-apps.jpg) | |
| bag | [context.py](https://github.com/colmwoods/PCPartsIreland/blob/main/bag/context.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/bag/context.py) | ![screenshot](documentation/validation/py-bag-context.jpg) | |
| bag | [models.py](https://github.com/colmwoods/PCPartsIreland/blob/main/bag/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/bag/models.py) | ![screenshot](documentation/validation/py-bag-models.jpg) | |
| bag | [tests.py](https://github.com/colmwoods/PCPartsIreland/blob/main/bag/tests.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/bag/tests.py) | ![screenshot](documentation/validation/py-bag-tests.jpg) | |
| bag | [urls.py](https://github.com/colmwoods/PCPartsIreland/blob/main/bag/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/bag/urls.py) | ![screenshot](documentation/validation/py-bag-urls.jpg) |  |
| bag | [views.py](https://github.com/colmwoods/PCPartsIreland/blob/main/bag/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/bag/views.py) | ![screenshot](documentation/validation/py-bag-views.jpg) | |
| checkout | [admin.py](https://github.com/colmwoods/PCPartsIreland/blob/main/checkout/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/checkout/admin.py) | ![screenshot](documentation/validation/py-checkout-admin.jpg) |  |
| checkout | [apps.py](https://github.com/colmwoods/PCPartsIreland/blob/main/checkout/apps.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/checkout/apps.py) | ![screenshot](documentation/validation/py-checkout-apps.jpg) | |
| checkout | [forms.py](https://github.com/colmwoods/PCPartsIreland/blob/main/checkout/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/checkout/forms.py) | ![screenshot](documentation/validation/py-checkout-forms.jpg) ||
| checkout | [models.py](https://github.com/colmwoods/PCPartsIreland/blob/main/checkout/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/checkout/models.py) | ![screenshot](documentation/validation/py-checkout-models.jpg) | |
| checkout | [tests.py](https://github.com/colmwoods/PCPartsIreland/blob/main/checkout/tests.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/checkout/tests.py) | ![screenshot](documentation/validation/py-checkout-tests.jpg) | |
| checkout | [urls.py](https://github.com/colmwoods/PCPartsIreland/blob/main/checkout/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/checkout/urls.py) | ![screenshot](documentation/validation/py-checkout-urls.jpg) | |
| checkout | [views.py](https://github.com/colmwoods/PCPartsIreland/blob/main/checkout/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/checkout/views.py) | ![screenshot](documentation/validation/py-checkout-views.jpg) | |
| faq | [admin.py](https://github.com/colmwoods/PCPartsIreland/blob/main/faq/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/faq/admin.py) | ![screenshot](documentation/validation/py-faq-admin.jpg) | |
| faq | [apps.py](https://github.com/colmwoods/PCPartsIreland/blob/main/faq/apps.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/faq/apps.py) | ![screenshot](documentation/validation/py-faq-apps.jpg) | |
| faq | [models.py](https://github.com/colmwoods/PCPartsIreland/blob/main/faq/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/faq/models.py) | ![screenshot](documentation/validation/py-faq-models.jpg) | |
| faq | [tests.py](https://github.com/colmwoods/PCPartsIreland/blob/main/faq/tests.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/faq/tests.py) | ![screenshot](documentation/validation/py-faq-tests.jpg) | |
| faq | [urls.py](https://github.com/colmwoods/PCPartsIreland/blob/main/faq/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/faq/urls.py) | ![screenshot](documentation/validation/py-faq-urls.jpg) | |
| faq | [views.py](https://github.com/colmwoods/PCPartsIreland/blob/main/faq/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/faq/views.py) | ![screenshot](documentation/validation/py-faq-views.jpg) | |
| form | [admin.py](https://github.com/colmwoods/PCPartsIreland/blob/main/form/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/form/admin.py) | ![screenshot](documentation/validation/py-form-admin.jpg) | |
| form | [apps.py](https://github.com/colmwoods/PCPartsIreland/blob/main/form/apps.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/form/apps.py) | ![screenshot](documentation/validation/py-form-apps.jpg) | |
| form | [forms.py](https://github.com/colmwoods/PCPartsIreland/blob/main/form/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/form/forms.py) | ![screenshot](documentation/validation/py-form-forms.jpg) | |
| form | [models.py](https://github.com/colmwoods/PCPartsIreland/blob/main/form/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/form/models.py) | ![screenshot](documentation/validation/py-form-models.jpg) | |
| form | [tests.py](https://github.com/colmwoods/PCPartsIreland/blob/main/form/tests.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/form/tests.py) | ![screenshot](documentation/validation/py-form-tests.jpg) | |
| form | [urls.py](https://github.com/colmwoods/PCPartsIreland/blob/main/form/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/form/urls.py) | ![screenshot](documentation/validation/py-form-urls.jpg) | |
| form | [views.py](https://github.com/colmwoods/PCPartsIreland/blob/main/form/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/form/views.py) | ![screenshot](documentation/validation/py-form-views.jpg) | |
| home | [admin.py](https://github.com/colmwoods/PCPartsIreland/blob/main/home/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/home/admin.py) | ![screenshot](documentation/validation/py-home-admin.jpg) |  |
| home | [apps.py](https://github.com/colmwoods/PCPartsIreland/blob/main/home/apps.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/home/apps.py) | ![screenshot](documentation/validation/py-home-apps.jpg) | |
| home | [models.py](https://github.com/colmwoods/PCPartsIreland/blob/main/home/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/home/models.py) | ![screenshot](documentation/validation/py-home-models.jpg) | |
| home | [tests.py](https://github.com/colmwoods/PCPartsIreland/blob/main/home/tests.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/home/tests.py) | ![screenshot](documentation/validation/py-home-tests.jpg) | |
| home | [urls.py](https://github.com/colmwoods/PCPartsIreland/blob/main/home/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/home/urls.py) | ![screenshot](documentation/validation/py-home-urls.jpg) | |
| home | [views.py](https://github.com/colmwoods/PCPartsIreland/blob/main/home/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/home/views.py) | ![screenshot](documentation/validation/py-home-views.jpg) | |
| pcpartsireland | [asgi.py](https://github.com/colmwoods/PCPartsIreland/blob/main/pcpartsireland/asgi.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/pcpartsireland/asgi.py) | ![screenshot](documentation/validation/py-pcpartsireland-asgi.jpg) | |
| pcpartsireland | [context_processors.py](https://github.com/colmwoods/PCPartsIreland/blob/main/pcpartsireland/context_processors.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/pcpartsireland/context_processors.py) | ![screenshot](documentation/validation/py-pcpartsireland-context_processors.jpg) | |
| pcpartsireland | [middleware.py](https://github.com/colmwoods/PCPartsIreland/blob/main/pcpartsireland/middleware.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/pcpartsireland/middleware.py) | ![screenshot](documentation/validation/py-pcpartsireland-middleware.jpg) | |
| pcpartsireland | [settings.py](https://github.com/colmwoods/PCPartsIreland/blob/main/pcpartsireland/settings.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/pcpartsireland/settings.py) | ![screenshot](documentation/validation/py-pcpartsireland-settings.jpg) | |
| pcpartsireland | [tests.py](https://github.com/colmwoods/PCPartsIreland/blob/main/pcpartsireland/tests.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/pcpartsireland/tests.py) | ![screenshot](documentation/validation/py-pcpartsireland-tests.jpg) | |
| pcpartsireland | [urls.py](https://github.com/colmwoods/PCPartsIreland/blob/main/pcpartsireland/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/pcpartsireland/urls.py) | ![screenshot](documentation/validation/py-pcpartsireland-urls.jpg) | |
| pcpartsireland | [views.py](https://github.com/colmwoods/PCPartsIreland/blob/main/pcpartsireland/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/pcpartsireland/views.py) | ![screenshot](documentation/validation/py-pcpartsireland-views.jpg) | |
| pcpartsireland | [wsgi.py](https://github.com/colmwoods/PCPartsIreland/blob/main/pcpartsireland/wsgi.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/pcpartsireland/wsgi.py) | ![screenshot](documentation/validation/py-pcpartsireland-wsgi.jpg) | |
| products | [admin.py](https://github.com/colmwoods/PCPartsIreland/blob/main/products/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/products/admin.py) | ![screenshot](documentation/validation/py-products-admin.jpg) |  |
| products | [apps.py](https://github.com/colmwoods/PCPartsIreland/blob/main/products/apps.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/products/apps.py) | ![screenshot](documentation/validation/py-products-apps.jpg) | |
| products | [forms.py](https://github.com/colmwoods/PCPartsIreland/blob/main/products/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/products/forms.py) | ![screenshot](documentation/validation/py-products-forms.jpg) | |
| products | [models.py](https://github.com/colmwoods/PCPartsIreland/blob/main/products/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/products/models.py) | ![screenshot](documentation/validation/py-products-models.jpg) | |
| products | [tests.py](https://github.com/colmwoods/PCPartsIreland/blob/main/products/tests.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/products/tests.py) | ![screenshot](documentation/validation/py-products-tests.jpg) | |
| products | [urls.py](https://github.com/colmwoods/PCPartsIreland/blob/main/products/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/products/urls.py) | ![screenshot](documentation/validation/py-products-urls.jpg) | |
| products | [views.py](https://github.com/colmwoods/PCPartsIreland/blob/main/products/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/products/views.py) | ![screenshot](documentation/validation/py-products-views.jpg) | |
| products | [widgets.py](https://github.com/colmwoods/PCPartsIreland/blob/main/products/widgets.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/products/widgets.py) | ![screenshot](documentation/validation/py-products-widgets.jpg) |  |
| products | [math_filters.py](https://github.com/colmwoods/PCPartsIreland/blob/main/products/templatetags/math_filters.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/products/templatetags/math_filters.py) | ![screenshot](documentation/validation/py-products-math_filters.jpg) | |
| profiles | [admin.py](https://github.com/colmwoods/PCPartsIreland/blob/main/profiles/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/profiles/admin.py) | ![screenshot](documentation/validation/py-profiles-admin.jpg) | |
| profiles | [apps.py](https://github.com/colmwoods/PCPartsIreland/blob/main/profiles/apps.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/profiles/apps.py) | ![screenshot](documentation/validation/py-profiles-apps.jpg) ||
| profiles | [forms.py](https://github.com/colmwoods/PCPartsIreland/blob/main/profiles/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/profiles/forms.py) | ![screenshot](documentation/validation/py-profiles-forms.jpg) | |
| profiles | [models.py](https://github.com/colmwoods/PCPartsIreland/blob/main/profiles/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/profiles/models.py) | ![screenshot](documentation/validation/py-profiles-models.jpg) | |
| profiles | [tests.py](https://github.com/colmwoods/PCPartsIreland/blob/main/profiles/tests.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/profiles/tests.py) | ![screenshot](documentation/validation/py-profiles-tests.jpg) | |
| profiles | [urls.py](https://github.com/colmwoods/PCPartsIreland/blob/main/profiles/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/profiles/urls.py) | ![screenshot](documentation/validation/py-profiles-urls.jpg) | |
| profiles | [views.py](https://github.com/colmwoods/PCPartsIreland/blob/main/profiles/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/profiles/views.py) | ![screenshot](documentation/validation/py-profiles-views.jpg) | |


## Responsiveness

I've tested my deployed project to check for responsiveness issues. Testing was performed using Chrome Developer Tools device toolbar across common viewport sizes to simulate different devices.

The following resolutions were used during testing:

- **Mobile:** 375 × 812 (typical smartphone viewport)
- **Tablet:** 768 × 1024 (standard tablet viewport)
- **Desktop:** 1920 × 1080 (full HD desktop display)

Each page was tested at these breakpoints to ensure layouts adapt correctly, navigation remains accessible, and no horizontal scrolling or layout overflow occurs.

| Page | Mobile | Tablet | Desktop | Notes |
| --- | --- | --- | --- | --- |
| Register | ![screenshot](documentation/responsiveness/mobile-register.jpg) | ![screenshot](documentation/responsiveness/tablet-register.jpg) | ![screenshot](documentation/responsiveness/desktop-register.jpg) | Works as expected |
| Login | ![screenshot](documentation/responsiveness/mobile-login.jpg) | ![screenshot](documentation/responsiveness/tablet-login.jpg) | ![screenshot](documentation/responsiveness/desktop-login.jpg) | Works as expected |
| Profile | ![screenshot](documentation/responsiveness/mobile-profile.jpg) | ![screenshot](documentation/responsiveness/tablet-profile.jpg) | ![screenshot](documentation/responsiveness/desktop-profile.jpg) | Works as expected |
| Home | ![screenshot](documentation/responsiveness/mobile-home.jpg) | ![screenshot](documentation/responsiveness/tablet-home.jpg) | ![screenshot](documentation/responsiveness/desktop-home.jpg) | Works as expected |
| Products | ![screenshot](documentation/responsiveness/mobile-products.jpg) | ![screenshot](documentation/responsiveness/tablet-products.jpg) | ![screenshot](documentation/responsiveness/desktop-products.jpg) | Works as expected, Logged in as superuser |
| Product Details | ![screenshot](documentation/responsiveness/mobile-product-details.jpg) | ![screenshot](documentation/responsiveness/tablet-product-details.jpg) | ![screenshot](documentation/responsiveness/desktop-product-details.jpg) | Works as expected, Logged in as superuser |
| Bag | ![screenshot](documentation/responsiveness/mobile-bag.jpg) | ![screenshot](documentation/responsiveness/tablet-bag.jpg) | ![screenshot](documentation/responsiveness/desktop-bag.jpg) | Works as expected |
| Checkout | ![screenshot](documentation/responsiveness/mobile-checkout.jpg) | ![screenshot](documentation/responsiveness/tablet-checkout.jpg) | ![screenshot](documentation/responsiveness/desktop-checkout.jpg) | Works as expected |
| Checkout Success | ![screenshot](documentation/responsiveness/mobile-checkout-success.jpg) | ![screenshot](documentation/responsiveness/tablet-checkout-success.jpg) | ![screenshot](documentation/responsiveness/desktop-checkout-success.jpg) | Works as expected |
| Add Product | ![screenshot](documentation/responsiveness/mobile-add-product.jpg) | ![screenshot](documentation/responsiveness/tablet-add-product.jpg) | ![screenshot](documentation/responsiveness/desktop-add-product.jpg) | Works as expected |
| Edit Product | ![screenshot](documentation/responsiveness/mobile-edit-product.jpg) | ![screenshot](documentation/responsiveness/tablet-edit-product.jpg) | ![screenshot](documentation/responsiveness/desktop-edit-product.jpg) | Works as expected |
| Newsletter | ![screenshot](documentation/responsiveness/mobile-newsletter.jpg) | ![screenshot](documentation/responsiveness/tablet-newsletter.jpg) | ![screenshot](documentation/responsiveness/desktop-newsletter.jpg) | Works as expected |
| Contact | ![screenshot](documentation/responsiveness/mobile-contact.jpg) | ![screenshot](documentation/responsiveness/tablet-contact.jpg) | ![screenshot](documentation/responsiveness/desktop-contact.jpg) | Works as expected |
| 404 | ![screenshot](documentation/responsiveness/mobile-404.jpg) | ![screenshot](documentation/responsiveness/tablet-404.jpg) | ![screenshot](documentation/responsiveness/desktop-404.jpg) | Works as expected |
| Search Results | ![screenshot](documentation/responsiveness/mobile-search-results.jpg) | ![screenshot](documentation/responsiveness/tablet-search-results.jpg) | ![screenshot](documentation/responsiveness/desktop-search-results.jpg) | Works as expected |
| FAQ | ![screenshot](documentation/responsiveness/mobile-faq.jpg) | ![screenshot](documentation/responsiveness/tablet-faq.jpg) | ![screenshot](documentation/responsiveness/desktop-faq.jpg) | Works as expected |
| Returns | ![screenshot](documentation/responsiveness/mobile-returns.jpg) | ![screenshot](documentation/responsiveness/tablet-returns.jpg) | ![screenshot](documentation/responsiveness/desktop-returns.jpg) | Works as expected |
| Logout | ![screenshot](documentation/responsiveness/mobile-logout.jpg) | ![screenshot](documentation/responsiveness/tablet-logout.jpg) | ![screenshot](documentation/responsiveness/desktop-logout.jpg) | Works as expected |
| Password Reset | ![screenshot](documentation/responsiveness/mobile-password-reset.jpg) | ![screenshot](documentation/responsiveness/tablet-password-reset.jpg) | ![screenshot](documentation/responsiveness/desktop-password-reset.jpg) | Works as expected |
| Password Reset Confirm | ![screenshot](documentation/responsiveness/mobile-password-reset-confirm.jpg) | ![screenshot](documentation/responsiveness/tablet-password-reset-confirm.jpg) | ![screenshot](documentation/responsiveness/desktop-password-reset-confirm.jpg) | Works as expected |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Page | Chrome | Firefox | Safari | Edge | Brave | Opera | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Register | ![screenshot](documentation/browsers/chrome-register.jpg) | ![screenshot](documentation/browsers/firefox-register.jpg) | ![screenshot](documentation/browsers/safari-register.jpg) | ![screenshot](documentation/browsers/edge-register.jpg) | ![screenshot](documentation/browsers/brave-register.jpg) | ![screenshot](documentation/browsers/opera-register.jpg) | Works as expected |
| Login | ![screenshot](documentation/browsers/chrome-login.jpg) | ![screenshot](documentation/browsers/firefox-login.jpg) | ![screenshot](documentation/browsers/safari-login.jpg) | ![screenshot](documentation/browsers/edge-login.jpg) | ![screenshot](documentation/browsers/brave-login.jpg) | ![screenshot](documentation/browsers/opera-login.jpg) | Works as expected |
| Profile | ![screenshot](documentation/browsers/chrome-profile.jpg) | ![screenshot](documentation/browsers/firefox-profile.jpg) | ![screenshot](documentation/browsers/safari-profile.jpg) | ![screenshot](documentation/browsers/edge-profile.jpg) | ![screenshot](documentation/browsers/brave-profile.jpg) | ![screenshot](documentation/browsers/opera-profile.jpg) | Works as expected |
| Home | ![screenshot](documentation/browsers/chrome-home.jpg) | ![screenshot](documentation/browsers/firefox-home.jpg) | ![screenshot](documentation/browsers/safari-home.jpg) | ![screenshot](documentation/browsers/edge-home.jpg) | ![screenshot](documentation/browsers/brave-home.jpg) | ![screenshot](documentation/browsers/opera-home.jpg) | Works as expected |
| Products | ![screenshot](documentation/browsers/chrome-products.jpg) | ![screenshot](documentation/browsers/firefox-products.jpg) | ![screenshot](documentation/browsers/safari-products.jpg) | ![screenshot](documentation/browsers/edge-products.jpg) | ![screenshot](documentation/browsers/brave-products.jpg) | ![screenshot](documentation/browsers/opera-products.jpg) | Works as expected |
| Product Details | ![screenshot](documentation/browsers/chrome-product-details.jpg) | ![screenshot](documentation/browsers/firefox-product-details.jpg) | ![screenshot](documentation/browsers/safari-product-details.jpg) | ![screenshot](documentation/browsers/edge-product-details.jpg) | ![screenshot](documentation/browsers/brave-product-details.jpg) | ![screenshot](documentation/browsers/opera-product-details.jpg) | Works as expected |
| Bag | ![screenshot](documentation/browsers/chrome-bag.jpg) | ![screenshot](documentation/browsers/firefox-bag.jpg) | ![screenshot](documentation/browsers/safari-bag.jpg) | ![screenshot](documentation/browsers/edge-bag.jpg) | ![screenshot](documentation/browsers/brave-bag.jpg) | ![screenshot](documentation/browsers/opera-bag.jpg) | Works as expected |
| Checkout | ![screenshot](documentation/browsers/chrome-checkout.jpg) | ![screenshot](documentation/browsers/firefox-checkout.jpg) | ![screenshot](documentation/browsers/safari-checkout.jpg) | ![screenshot](documentation/browsers/edge-checkout.jpg) | ![screenshot](documentation/browsers/brave-checkout.jpg) | ![screenshot](documentation/browsers/opera-checkout.jpg) | Works as expected |
| Checkout Success | ![screenshot](documentation/browsers/chrome-checkout-success.jpg) | ![screenshot](documentation/browsers/firefox-checkout-success.jpg) | ![screenshot](documentation/browsers/safari-checkout-success.jpg) | ![screenshot](documentation/browsers/edge-checkout-success.jpg) | ![screenshot](documentation/browsers/brave-checkout-success.jpg) | ![screenshot](documentation/browsers/opera-checkout-success.jpg) | Works as expected |
| Add Product | ![screenshot](documentation/browsers/chrome-add-product.jpg) | ![screenshot](documentation/browsers/firefox-add-product.jpg) | ![screenshot](documentation/browsers/safari-add-product.jpg) | ![screenshot](documentation/browsers/edge-add-product.jpg) | ![screenshot](documentation/browsers/brave-add-product.jpg) | ![screenshot](documentation/browsers/opera-add-product.jpg) | Works as expected |
| Edit Product | ![screenshot](documentation/browsers/chrome-edit-product.jpg) | ![screenshot](documentation/browsers/firefox-edit-product.jpg) | ![screenshot](documentation/browsers/safari-edit-product.jpg) | ![screenshot](documentation/browsers/edge-edit-product.jpg) | ![screenshot](documentation/browsers/brave-edit-product.jpg) | ![screenshot](documentation/browsers/opera-edit-product.jpg) | Works as expected |
| Newsletter | ![screenshot](documentation/browsers/chrome-newsletter.jpg) | ![screenshot](documentation/browsers/firefox-newsletter.jpg) | ![screenshot](documentation/browsers/safari-newsletter.jpg) | ![screenshot](documentation/browsers/edge-newsletter.jpg) | ![screenshot](documentation/browsers/brave-newsletter.jpg) | ![screenshot](documentation/browsers/opera-newsletter.jpg) | Works as expected |
| Contact | ![screenshot](documentation/browsers/chrome-contact.jpg) | ![screenshot](documentation/browsers/firefox-contact.jpg) | ![screenshot](documentation/browsers/safari-contact.jpg) | ![screenshot](documentation/browsers/edge-contact.jpg) | ![screenshot](documentation/browsers/brave-contact.jpg) | ![screenshot](documentation/browsers/opera-contact.jpg) | Works as expected |
| 404 | ![screenshot](documentation/browsers/chrome-404.jpg) | ![screenshot](documentation/browsers/firefox-404.jpg) | ![screenshot](documentation/browsers/safari-404.jpg) | ![screenshot](documentation/browsers/edge-404.jpg) | ![screenshot](documentation/browsers/brave-404.jpg) | ![screenshot](documentation/browsers/opera-404.jpg) | Works as expected |
| Search Results | ![screenshot](documentation/browsers/chrome-search-results.jpg) | ![screenshot](documentation/browsers/firefox-search-results.jpg) | ![screenshot](documentation/browsers/safari-search-results.jpg) | ![screenshot](documentation/browsers/edge-search-results.jpg) | ![screenshot](documentation/browsers/brave-search-results.jpg) | ![screenshot](documentation/browsers/opera-search-results.jpg) | Works as expected |
| FAQ | ![screenshot](documentation/browsers/chrome-faq.jpg) | ![screenshot](documentation/browsers/firefox-faq.jpg) | ![screenshot](documentation/browsers/safari-faq.jpg) | ![screenshot](documentation/browsers/edge-faq.jpg) | ![screenshot](documentation/browsers/brave-faq.jpg) | ![screenshot](documentation/browsers/opera-faq.jpg) | Works as expected |
| Logout | ![screenshot](documentation/browsers/chrome-logout.jpg) | ![screenshot](documentation/browsers/firefox-logout.jpg) | ![screenshot](documentation/browsers/safari-logout.jpg) | ![screenshot](documentation/browsers/edge-logout.jpg) | ![screenshot](documentation/browsers/brave-logout.jpg) | ![screenshot](documentation/browsers/opera-logout.jpg) | Works as expected |
| Returns | ![screenshot](documentation/browsers/chrome-returns.jpg) | ![screenshot](documentation/browsers/firefox-returns.jpg) | ![screenshot](documentation/browsers/safari-returns.jpg) | ![screenshot](documentation/browsers/edge-returns.jpg) | ![screenshot](documentation/browsers/brave-returns.jpg) | ![screenshot](documentation/browsers/opera-returns.jpg) | Works as expected |
| Password Reset | ![screenshot](documentation/browsers/chrome-password-reset.jpg) | ![screenshot](documentation/browsers/firefox-password-reset.jpg) | ![screenshot](documentation/browsers/safari-password-reset.jpg) | ![screenshot](documentation/browsers/edge-password-reset.jpg) | ![screenshot](documentation/browsers/brave-password-reset.jpg) | ![screenshot](documentation/browsers/opera-password-reset.jpg) | Works as expected |
| Password Reset Confirm | ![screenshot](documentation/browsers/chrome-password-reset-confirm.jpg) | ![screenshot](documentation/browsers/firefox-password-reset-confirm.jpg) | ![screenshot](documentation/browsers/safari-password-reset-confirm.jpg) | ![screenshot](documentation/browsers/edge-password-reset-confirm.jpg) | ![screenshot](documentation/browsers/brave-password-reset-confirm.jpg) | ![screenshot](documentation/browsers/opera-password-reset-confirm.jpg) | Works as expected |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues. Some warnings are outside of my control, and mobile results tend to be lower than desktop.

| Page | Mobile | Desktop |
| --- | --- | --- |
| Register | ![screenshot](documentation/lighthouse/mobile-register.jpg) | ![screenshot](documentation/lighthouse/desktop-register.jpg) |
| Login | ![screenshot](documentation/lighthouse/mobile-login.jpg) | ![screenshot](documentation/lighthouse/desktop-login.jpg) |
| Profile | ![screenshot](documentation/lighthouse/mobile-profile.jpg) | ![screenshot](documentation/lighthouse/desktop-profile.jpg) |
| Home | ![screenshot](documentation/lighthouse/mobile-home.jpg) | ![screenshot](documentation/lighthouse/desktop-home.jpg) |
| Products | ![screenshot](documentation/lighthouse/mobile-products.jpg) | ![screenshot](documentation/lighthouse/desktop-products.jpg) |
| Product Details | ![screenshot](documentation/lighthouse/mobile-product-details.jpg) | ![screenshot](documentation/lighthouse/desktop-product-details.jpg) |
| Bag | ![screenshot](documentation/lighthouse/mobile-bag.jpg) | ![screenshot](documentation/lighthouse/desktop-bag.jpg) |
| Checkout | ![screenshot](documentation/lighthouse/mobile-checkout.jpg) | ![screenshot](documentation/lighthouse/desktop-checkout.jpg) |
| Checkout Success | ![screenshot](documentation/lighthouse/mobile-checkout-success.jpg) | ![screenshot](documentation/lighthouse/desktop-checkout-success.jpg) |
| Add Product | ![screenshot](documentation/lighthouse/mobile-add-product.jpg) | ![screenshot](documentation/lighthouse/desktop-add-product.jpg) |
| Edit Product | ![screenshot](documentation/lighthouse/mobile-edit-product.jpg) | ![screenshot](documentation/lighthouse/desktop-edit-product.jpg) |
| Newsletter | ![screenshot](documentation/lighthouse/mobile-newsletter.jpg) | ![screenshot](documentation/lighthouse/desktop-newsletter.jpg) |
| Contact | ![screenshot](documentation/lighthouse/mobile-contact.jpg) | ![screenshot](documentation/lighthouse/desktop-contact.jpg) |
| 404 | ![screenshot](documentation/lighthouse/mobile-404.jpg) | ![screenshot](documentation/lighthouse/desktop-404.jpg) |
| Search Results | ![screenshot](documentation/lighthouse/mobile-search-results.jpg) | ![screenshot](documentation/lighthouse/desktop-search-results.jpg) |
| FAQ | ![screenshot](documentation/lighthouse/mobile-faq.jpg) | ![screenshot](documentation/lighthouse/desktop-faq.jpg) |
| Logout | ![screenshot](documentation/lighthouse/mobile-logout.jpg) | ![screenshot](documentation/lighthouse/desktop-logout.jpg) |
| Returns | ![screenshot](documentation/lighthouse/mobile-returns.jpg) | ![screenshot](documentation/lighthouse/desktop-returns.jpg) |
| Password Reset | ![screenshot](documentation/lighthouse/mobile-password-reset.jpg) | ![screenshot](documentation/lighthouse/desktop-password-reset.jpg) |
| Password Reset Confirm | ![screenshot](documentation/lighthouse/mobile-password-reset-confirm.jpg) | ![screenshot](documentation/lighthouse/desktop-password-reset-confirm.jpg) |

## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Screenshot |
| --- | --- | --- | --- | --- |
| Products | Feature is expected to allow users to browse products without registration. | Opened product pages as a guest user. | Products were fully accessible without requiring registration. | ![screenshot](documentation/defensive/products.jpg) |
|  | Feature is expected to sort products by price and name. | Tested sorting options for price (low-to-high/high-to-low) and name (alphabetical). | Sorting worked correctly for all options. | ![screenshot](documentation/defensive/sorting.jpg) |
|  | Feature is expected to filter products by category. | Applied category filters while browsing products. | Filters worked as expected, displaying only relevant products. | ![screenshot](documentation/defensive/filtering.jpg) |
|  | Feature is expected to show detailed product information. | Clicked on individual products to view details. | Product details (description, price, image) were displayed correctly. | ![screenshot](documentation/defensive/product-details.jpg) |
| Shopping Cart | Feature is expected to allow customers to add items to the cart with quantity controls. | Added products to the cart and adjusted quantities. | Items were added successfully, and quantities updated as expected. | ![screenshot](documentation/defensive/add-to-cart.jpg) |
|  | Feature is expected to allow customers to view and manage their cart. | Opened the cart page and edited cart contents. | Cart contents were displayed, updated, and removed correctly. | ![screenshot](documentation/defensive/manage-cart.jpg) |
| Checkout | Feature is expected to display cart items, grand total, and input fields for checkout. | Proceeded to checkout with items in the cart. | Checkout page displayed cart items, total, and input fields as expected. | ![screenshot](documentation/defensive/checkout.jpg) |
|  | Feature is expected to allow secure payment via Stripe. | Entered valid card details using Stripe at checkout. | Payment was processed securely, and an order confirmation page was displayed. | ![screenshot](documentation/defensive/stripe-payment.jpg) |
|  | Feature is expected to send a confirmation email after purchase. | Completed a purchase and checked email inbox. | Confirmation email was received with order details. | ![screenshot](documentation/defensive/confirmation-email.jpg) |
|  | Feature is expected to display an order confirmation page with an order number. | Completed a purchase. | Order confirmation page displayed successfully with an order number. | ![screenshot](documentation/defensive/order-confirmation.jpg) |
| Account Management | Feature is expected to allow returning customers to log in and view past orders. | Logged in as a returning customer and accessed order history. | Past orders were displayed correctly in the account section. | ![screenshot](documentation/defensive/order-history.jpg) |
|  | Feature is expected to remember the shipping address for returning customers. | Completed multiple checkouts as a returning customer. | Shipping address was pre-filled on subsequent purchases. | ![screenshot](documentation/defensive/saved-address.jpg) |
| Admin Features | Feature is expected to allow the site owner to create new products. | Created new products with valid data (name, price, description, image, category). | Products were added successfully and displayed on the site. | ![screenshot](documentation/defensive/create-product.jpg) |
|  | Feature is expected to allow the site owner to update product details. | Edited product details as an admin user. | Product updates were saved and displayed correctly. | ![screenshot](documentation/defensive/update-product.jpg) |
|  | Feature is expected to allow the site owner to delete products. | Deleted a product from the inventory. | Product was removed successfully from the site, after being prompted to confirm first. | ![screenshot](documentation/defensive/delete-product.jpg) |
| Orders | Feature is expected to allow the site owner to view all orders placed. | Accessed the orders dashboard as an admin user. | All orders were displayed correctly. | ![screenshot](documentation/defensive/view-orders.jpg) |
| Newsletter | Feature is expected to allow users to sign up for the newsletter. | Submitted valid email addresses for newsletter registration. | Email addresses were successfully added to the newsletter list. | ![screenshot](documentation/defensive/newsletter.jpg) |
| 404 Error Page | Feature is expected to display a 404 error page for non-existent pages. | Navigated to an invalid URL (e.g., `/test`). | A custom 404 error page was displayed as expected. | ![screenshot](documentation/defensive/404.jpg) |

## User Story Testing

| Target | Expectation | Outcome | Screenshot |
| --- | --- | --- | --- |
| As a guest user | I would like to browse products without needing to register | so that I can shop freely before deciding to create an account. | ![screenshot](documentation/user-stories/userstory01.jpg) |
| As a guest user | I would like to be prompted to create an account or log in at checkout | so that I can complete my purchase and track my order history. | ![screenshot](documentation/user-stories/userstory02.jpg) |
| As a user | I would like to sign up to the site's newsletter | so that I can stay up to date with any upcoming sales or promotions. | ![screenshot](documentation/user-stories/userstory03.jpg) |
| As a customer | I would like to browse various product categories (clothing, toys, jewelry, kitchen gadgets, etc.) | so that I can easily find what I'm looking for. | ![screenshot](documentation/user-stories/userstory04.jpg) |
| As a customer | I would like to sort products by price (low-to-high/high-to-low) and name (alphabetical) | so that I can quickly organize items in a way that suits my shopping style. | ![screenshot](documentation/user-stories/userstory05.jpg) |
| As a customer | I would like to filter products by category | so that I can narrow down the products to the types I am most interested in. | ![screenshot](documentation/user-stories/userstory06.jpg) |
| As a customer | I would like to click on individual products to view more details (description, price, image, etc.) | so that I can make an informed decision about my purchase. | ![screenshot](documentation/user-stories/userstory07.jpg) |
| As a customer | I would like to add items to my shopping cart using quantity increment/decrement buttons | so that I can adjust how many units of a product I want before checkout. | ![screenshot](documentation/user-stories/userstory08.jpg) |
| As a customer | I would like to view and manage my shopping cart | so that I can review, add, or remove items before proceeding to checkout. | ![screenshot](documentation/user-stories/userstory09.jpg) |
| As a customer | I would like to adjust the quantity of items in my cart | so that I can modify my purchase preferences without leaving the cart. | ![screenshot](documentation/user-stories/userstory10.jpg) |
| As a customer | I would like to remove items from my cart | so that I can remove products I no longer wish to buy. | ![screenshot](documentation/user-stories/userstory11.jpg) |
| As a customer | I would like to proceed to checkout where I see my cart items, grand total, and input my name, email, shipping address, and card details | so that I can complete my purchase. | ![screenshot](documentation/user-stories/userstory12.jpg) |
| As a customer | I would like to receive a confirmation email after my purchase | so that I can have a record of my transaction and order details. | ![screenshot](documentation/user-stories/userstory13.jpg) |
| As a customer | I would like to see an order confirmation page with a checkout order number after completing my purchase | so that I know my order has been successfully placed. | ![screenshot](documentation/user-stories/userstory14.jpg) |
| As a customer | I would like to securely enter my card details using Stripe at checkout | so that I can feel confident my payment information is protected. | ![screenshot](documentation/user-stories/userstory15.jpg) |
| As a returning customer | I would like to be able to log in and view my past orders | so that I can track my previous purchases and order history. | ![screenshot](documentation/user-stories/userstory16.jpg) |
| As a returning customer | I would like the checkout process to remember my shipping address | so that future purchases are quicker and easier. | ![screenshot](documentation/user-stories/userstory17.jpg) |
| As a site owner | I would like to create new products with a name, description, price, images, and category | so that I can add additional items to the store inventory. | ![screenshot](documentation/user-stories/userstory18.jpg) |
| As a site owner | I would like to update product details (name, price, description, image, category) at any time | so that I can keep my product listings accurate and up to date. | ![screenshot](documentation/user-stories/userstory19.jpg) |
| As a site owner | I would like to delete products that are no longer available or relevant | so that I can maintain a clean and accurate inventory. | ![screenshot](documentation/user-stories/userstory20.jpg) |
| As a site owner | I would like to view all orders placed on the website | so that I can track and manage customer purchases. | ![screenshot](documentation/user-stories/userstory21.jpg) |
| As a site owner | I would like to manage product categories | so that I can ensure items are correctly organized and easy for customers to find. | ![screenshot](documentation/user-stories/userstory22.jpg) |
| As a user | I would like to see a 404 error page if I get lost | so that it's obvious that I've stumbled upon a page that doesn't exist. | ![screenshot](documentation/user-stories/userstory23.jpg) |

## Automated Testing

I have conducted a series of automated tests on my application.

> [!NOTE]  
> I fully acknowledge and understand that, in a real-world scenario, an extensive set of additional tests would be more comprehensive.

### Python (Unit Testing)

Automated testing was implemented using Django’s built-in testing framework alongside the `coverage` package to measure code coverage.

A total of 38 unit tests were written to validate core application functionality, including product browsing, checkout processing, and user profile management. External services such as Stripe payments and email functionality were mocked to ensure reliable and isolated test execution.

The application achieved an overall test coverage of **86%**, demonstrating strong coverage across key components such as models, forms, and business logic.

![screenshot](documentation/automation/html-coverage.jpg)

While some view logic has slightly lower coverage due to UI-related complexity, the most critical functionality of the application is thoroughly tested, ensuring reliability and maintainability.

## Bugs

### Fixed Bugs

[![GitHub issue custom search](https://img.shields.io/github/issues-search/colmwoods/PCPartsIreland?query=is%3Aissue%20is%3Aclosed%20label%3Abug&label=Fixed%20Bugs&color=green)](https://www.github.com/colmwoods/PCPartsIreland/issues?q=is%3Aissue+is%3Aclosed+label%3Abug)

I've used [GitHub Issues](https://www.github.com/colmwoods/PCPartsIreland/issues) to track and manage bugs and issues during the development stages of my project.

All previously closed/fixed bugs can be tracked [here](https://www.github.com/colmwoods/PCPartsIreland/issues?q=is%3Aissue+is%3Aclosed+label%3Abug).

![screenshot](documentation/bugs/gh-issues-closed.jpg)

### Unfixed Bugs

[![GitHub issue custom search](https://img.shields.io/github/issues-search/colmwoods/PCPartsIreland?query=is%3Aissue%2Bis%3Aopen%2Blabel%3Abug&label=Unfixed%20Bugs&color=red)](https://www.github.com/colmwoods/PCPartsIreland/issues?q=is%3Aissue+is%3Aopen+label%3Abug)

Any remaining open issues can be tracked [here](https://www.github.com/colmwoods/PCPartsIreland/issues?q=is%3Aissue+is%3Aopen+label%3Abug).

![screenshot](documentation/bugs/gh-issues-open.jpg)

### Known Issues

| Issue | Screenshot |
| --- | --- |
| The project is designed to be responsive from `375px` and upwards, in line with the material taught on the course LMS. Minor layout inconsistencies may occur on extra-wide (e.g. 4k/8k monitors), or smart-display devices (e.g. Nest Hub, Smart Watches, Gameboy Color, etc.), as these resolutions are outside the project’s scope. | ![screenshot](documentation/issues/poor-responsiveness.jpg) |
| If a product is in your bag/cart, but then gets deleted from the database, it throws errors from the session storage memory. | ![screenshot](documentation/issues/session-storage.jpg) |

> [!IMPORTANT]  
> There are no remaining bugs that I am aware of, though, even after thorough testing, I cannot rule out the possibility.