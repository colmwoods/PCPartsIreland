# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.

In the following sections, I outline the manual and automated testing conducted on PCPartsIreland to ensure the application works correctly, securely, and provides a smooth user experience.

---

## Code Validation

All custom-written code files were validated using industry-standard validation tools. External libraries and frameworks (Bootstrap, Stripe, Django Allauth, etc.) were not validated as they are third-party dependencies.

---

### HTML

I used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all HTML templates.

Public pages were validated using **Validate by URI** from the deployed site.  
Authenticated pages containing Django/Jinja syntax were validated by copying the compiled page source and using **Validate by Input**.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| home | [index.html](https://github.com/colmwoods/PCPartsIreland/blob/main/home/templates/home/index.html) | Validated via deployed URL | ![screenshot](documentation/validation/html-home-index.png) | Homepage displaying featured products, navigation menu, and promotional content. Publicly accessible landing page of the site. |
| templates | [login.html](https://github.com/colmwoods/PCPartsIreland/blob/main/templates/account/login.html) | Compiled source validated | ![screenshot](documentation/validation/html-templates-login.png) | User authentication page allowing registered users to securely log into their account using Django Allauth. |
| templates | [logout.html](https://github.com/colmwoods/PCPartsIreland/blob/main/templates/account/logout.html) | Compiled source validated | ![screenshot](documentation/validation/html-templates-logout.png) | Logout confirmation page that securely ends the user session. |
| templates | [password_reset.html](https://github.com/colmwoods/PCPartsIreland/blob/main/templates/account/password_reset.html) | Compiled source validated | ![screenshot](documentation/validation/html-templates-password_reset.png) | Allows users to request a password reset email by submitting their registered email address. |
| templates | [password_reset_from_key.html](https://github.com/colmwoods/PCPartsIreland/blob/main/templates/account/password_reset_from_key.html) | Compiled source validated | ![screenshot](documentation/validation/html-templates-password_reset_from_key.png) | Allows users to securely set a new password using a tokenized reset link sent via email. |
| templates | [signup.html](https://github.com/colmwoods/PCPartsIreland/blob/main/templates/account/signup.html) | Compiled source validated | ![screenshot](documentation/validation/html-templates-signup.png) | User registration page enabling new customers to create an account. Validation warnings originate from Django Allauth and are outside custom code scope. |

All custom HTML templates passed validation. Any warnings present are related to Django Allauth and third-party integrations.



### CSS

I used the recommended CSS Jigsaw Validator to validate all custom CSS files used within PCPartsIreland.com.

Validator used:
https://jigsaw.w3.org/css-validator/

Primary stylesheet validated via deployed site URI:
https://jigsaw.w3.org/css-validator/validator?uri=https://pcpartsireland-1cfc0205aac1.herokuapp.com

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| static | [base.css](https://github.com/colmwoods/PCPartsIreland/blob/main/static/css/base.css) | Validated via deployed URI | ![screenshot](documentation/validation/css-static-base.png) | Main stylesheet controlling layout, navigation bar, product grid, cart layout, responsive breakpoints, and checkout styling. |

All custom CSS passed validation successfully. Any warnings shown were related to Bootstrap and are external dependencies.

---

### JavaScript

I used the recommended JSHint Validator to validate all custom JavaScript files used within PCPartsIreland.com.

Validator used:
https://jshint.com

Each JavaScript file includes:

`/* jshint esversion: 11 */`

Warnings relating to Stripe or Bootstrap are expected, as these are third-party libraries required for secure payment processing and UI behaviour.

All custom JavaScript passed validation and functions correctly across product quantity updates, cart management, and Stripe payment handling.

---

### Python

I used the recommended PEP8 CI Python Linter to validate all custom Python files.

Linter used:
https://pep8ci.herokuapp.com

Each file was validated using its raw GitHub URL.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| PCPartsIreland | [middleware.py](https://github.com/colmwoods/PCPartsIreland/blob/main/PCPartsIreland/middleware.py) | https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/PCPartsIreland/middleware.py | ![screenshot](documentation/validation/py-PCPartsIreland-middleware.png) | Handles custom middleware logic. |
| PCPartsIreland | [settings.py](https://github.com/colmwoods/PCPartsIreland/blob/main/PCPartsIreland/settings.py) | https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/PCPartsIreland/settings.py | ![screenshot](documentation/validation/py-PCPartsIreland-settings.png) | Default Django settings with secure configuration. |
| PCPartsIreland | [urls.py](https://github.com/colmwoods/PCPartsIreland/blob/main/PCPartsIreland/urls.py) | https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/PCPartsIreland/urls.py | ![screenshot](documentation/validation/py-PCPartsIreland-urls.png) | Global URL routing. |
| home | [admin.py](https://github.com/colmwoods/PCPartsIreland/blob/main/home/admin.py) | https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/home/admin.py | ![screenshot](documentation/validation/py-home-admin.png) | Admin registration for models. |
| home | [models.py](https://github.com/colmwoods/PCPartsIreland/blob/main/home/models.py) | https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/home/models.py | ![screenshot](documentation/validation/py-home-models.png) | Product and related data models. |
| home | [tests.py](https://github.com/colmwoods/PCPartsIreland/blob/main/home/tests.py) | https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/home/tests.py | ![screenshot](documentation/validation/py-home-tests.png) | Unit testing structure. |
| home | [urls.py](https://github.com/colmwoods/PCPartsIreland/blob/main/home/urls.py) | https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/home/urls.py | ![screenshot](documentation/validation/py-home-urls.png) | App-level routing. |
| home | [views.py](https://github.com/colmwoods/PCPartsIreland/blob/main/home/views.py) | https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/home/views.py | ![screenshot](documentation/validation/py-home-views.png) | View logic rendering homepage and product pages. |
|  | [manage.py](https://github.com/colmwoods/PCPartsIreland/blob/main/manage.py) | https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PCPartsIreland/main/manage.py | ![screenshot](documentation/validation/py--manage.png) | Django project entry file. |

All custom Python files passed validation. Default Django validator lines use `# noqa` where appropriate.

---

## Responsiveness

The deployed PCPartsIreland.com site was tested using Chrome Developer Tools device emulator and real device scaling across:

- Mobile (375px)
- Tablet (768px)
- Desktop (1920px)

| Page | Mobile | Tablet | Desktop | Notes |
| --- | --- | --- | --- | --- |
| Register | ![screenshot](documentation/responsiveness/mobile-register.png) | ![screenshot](documentation/responsiveness/tablet-register.png) | ![screenshot](documentation/responsiveness/desktop-register.png) | Works as expected |
| Login | ![screenshot](documentation/responsiveness/mobile-login.png) | ![screenshot](documentation/responsiveness/tablet-login.png) | ![screenshot](documentation/responsiveness/desktop-login.png) | Works as expected |
| Profile | ![screenshot](documentation/responsiveness/mobile-profile.png) | ![screenshot](documentation/responsiveness/tablet-profile.png) | ![screenshot](documentation/responsiveness/desktop-profile.png) | Works as expected |
| Home | ![screenshot](documentation/responsiveness/mobile-home.png) | ![screenshot](documentation/responsiveness/tablet-home.png) | ![screenshot](documentation/responsiveness/desktop-home.png) | Works as expected |
| Products | ![screenshot](documentation/responsiveness/mobile-products.png) | ![screenshot](documentation/responsiveness/tablet-products.png) | ![screenshot](documentation/responsiveness/desktop-products.png) | Works as expected |
| Product Details | ![screenshot](documentation/responsiveness/mobile-product-details.png) | ![screenshot](documentation/responsiveness/tablet-product-details.png) | ![screenshot](documentation/responsiveness/desktop-product-details.png) | Works as expected |
| Bag | ![screenshot](documentation/responsiveness/mobile-bag.png) | ![screenshot](documentation/responsiveness/tablet-bag.png) | ![screenshot](documentation/responsiveness/desktop-bag.png) | Works as expected |
| Checkout | ![screenshot](documentation/responsiveness/mobile-checkout.png) | ![screenshot](documentation/responsiveness/tablet-checkout.png) | ![screenshot](documentation/responsiveness/desktop-checkout.png) | Works as expected |
| Checkout Success | ![screenshot](documentation/responsiveness/mobile-checkout-success.png) | ![screenshot](documentation/responsiveness/tablet-checkout-success.png) | ![screenshot](documentation/responsiveness/desktop-checkout-success.png) | Works as expected |
| Add Product | ![screenshot](documentation/responsiveness/mobile-add-product.png) | ![screenshot](documentation/responsiveness/tablet-add-product.png) | ![screenshot](documentation/responsiveness/desktop-add-product.png) | Works as expected |
| Edit Product | ![screenshot](documentation/responsiveness/mobile-edit-product.png) | ![screenshot](documentation/responsiveness/tablet-edit-product.png) | ![screenshot](documentation/responsiveness/desktop-edit-product.png) | Works as expected |
| Newsletter | ![screenshot](documentation/responsiveness/mobile-newsletter.png) | ![screenshot](documentation/responsiveness/tablet-newsletter.png) | ![screenshot](documentation/responsiveness/desktop-newsletter.png) | Works as expected |
| Contact | ![screenshot](documentation/responsiveness/mobile-contact.png) | ![screenshot](documentation/responsiveness/tablet-contact.png) | ![screenshot](documentation/responsiveness/desktop-contact.png) | Works as expected |
| 404 | ![screenshot](documentation/responsiveness/mobile-404.png) | ![screenshot](documentation/responsiveness/tablet-404.png) | ![screenshot](documentation/responsiveness/desktop-404.png) | Works as expected |

All responsive layouts display correctly and maintain usability across device sizes.

---

## Browser Compatibility

PCPartsIreland.com was tested across multiple browsers:

- Chrome – https://www.google.com/chrome  
- Firefox – https://www.mozilla.org/firefox/  
- Safari – https://support.apple.com/downloads/safari  

| Page | Chrome | Firefox | Safari | Notes |
| --- | --- | --- | --- | --- |
| Register | ![screenshot](documentation/browsers/chrome-register.png) | ![screenshot](documentation/browsers/firefox-register.png) | ![screenshot](documentation/browsers/safari-register.png) | Works as expected |
| Login | ![screenshot](documentation/browsers/chrome-login.png) | ![screenshot](documentation/browsers/firefox-login.png) | ![screenshot](documentation/browsers/safari-login.png) | Works as expected |
| Profile | ![screenshot](documentation/browsers/chrome-profile.png) | ![screenshot](documentation/browsers/firefox-profile.png) | ![screenshot](documentation/browsers/safari-profile.png) | Works as expected |
| Home | ![screenshot](documentation/browsers/chrome-home.png) | ![screenshot](documentation/browsers/firefox-home.png) | ![screenshot](documentation/browsers/safari-home.png) | Works as expected |
| Products | ![screenshot](documentation/browsers/chrome-products.png) | ![screenshot](documentation/browsers/firefox-products.png) | ![screenshot](documentation/browsers/safari-products.png) | Works as expected |
| Product Details | ![screenshot](documentation/browsers/chrome-product-details.png) | ![screenshot](documentation/browsers/firefox-product-details.png) | ![screenshot](documentation/browsers/safari-product-details.png) | Works as expected |
| Bag | ![screenshot](documentation/browsers/chrome-bag.png) | ![screenshot](documentation/browsers/firefox-bag.png) | ![screenshot](documentation/browsers/safari-bag.png) | Works as expected |
| Checkout | ![screenshot](documentation/browsers/chrome-checkout.png) | ![screenshot](documentation/browsers/firefox-checkout.png) | ![screenshot](documentation/browsers/safari-checkout.png) | Works as expected |
| Checkout Success | ![screenshot](documentation/browsers/chrome-checkout-success.png) | ![screenshot](documentation/browsers/firefox-checkout-success.png) | ![screenshot](documentation/browsers/safari-checkout-success.png) | Works as expected |
| Add Product | ![screenshot](documentation/browsers/chrome-add-product.png) | ![screenshot](documentation/browsers/firefox-add-product.png) | ![screenshot](documentation/browsers/safari-add-product.png) | Works as expected |
| Edit Product | ![screenshot](documentation/browsers/chrome-edit-product.png) | ![screenshot](documentation/browsers/firefox-edit-product.png) | ![screenshot](documentation/browsers/safari-edit-product.png) | Works as expected |
| Newsletter | ![screenshot](documentation/browsers/chrome-newsletter.png) | ![screenshot](documentation/browsers/firefox-newsletter.png) | ![screenshot](documentation/browsers/safari-newsletter.png) | Works as expected |
| Contact | ![screenshot](documentation/browsers/chrome-contact.png) | ![screenshot](documentation/browsers/firefox-contact.png) | ![screenshot](documentation/browsers/safari-contact.png) | Works as expected |
| 404 | ![screenshot](documentation/browsers/chrome-404.png) | ![screenshot](documentation/browsers/firefox-404.png) | ![screenshot](documentation/browsers/safari-404.png) | Works as expected |

All core e-commerce functionality operates consistently across browsers.

---

## Lighthouse Audit

Lighthouse audits were run on the deployed PCPartsIreland.com site.

Lighthouse documentation:
https://developer.chrome.com/docs/lighthouse

Chrome extension:
https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk

| Page | Mobile | Desktop |
| --- | --- | --- |
| Register | ![screenshot](documentation/lighthouse/mobile-register.png) | ![screenshot](documentation/lighthouse/desktop-register.png) |
| Login | ![screenshot](documentation/lighthouse/mobile-login.png) | ![screenshot](documentation/lighthouse/desktop-login.png) |
| Profile | ![screenshot](documentation/lighthouse/mobile-profile.png) | ![screenshot](documentation/lighthouse/desktop-profile.png) |
| Home | ![screenshot](documentation/lighthouse/mobile-home.png) | ![screenshot](documentation/lighthouse/desktop-home.png) |
| Products | ![screenshot](documentation/lighthouse/mobile-products.png) | ![screenshot](documentation/lighthouse/desktop-products.png) |
| Product Details | ![screenshot](documentation/lighthouse/mobile-product-details.png) | ![screenshot](documentation/lighthouse/desktop-product-details.png) |
| Bag | ![screenshot](documentation/lighthouse/mobile-bag.png) | ![screenshot](documentation/lighthouse/desktop-bag.png) |
| Checkout | ![screenshot](documentation/lighthouse/mobile-checkout.png) | ![screenshot](documentation/lighthouse/desktop-checkout.png) |
| Checkout Success | ![screenshot](documentation/lighthouse/mobile-checkout-success.png) | ![screenshot](documentation/lighthouse/desktop-checkout-success.png) |
| Add Product | ![screenshot](documentation/lighthouse/mobile-add-product.png) | ![screenshot](documentation/lighthouse/desktop-add-product.png) |
| Edit Product | ![screenshot](documentation/lighthouse/mobile-edit-product.png) | ![screenshot](documentation/lighthouse/desktop-edit-product.png) |
| Newsletter | ![screenshot](documentation/lighthouse/mobile-newsletter.png) | ![screenshot](documentation/lighthouse/desktop-newsletter.png) |
| Contact | ![screenshot](documentation/lighthouse/mobile-contact.png) | ![screenshot](documentation/lighthouse/desktop-contact.png) |
| 404 | ![screenshot](documentation/lighthouse/mobile-404.png) | ![screenshot](documentation/lighthouse/desktop-404.png) |

Mobile scores are naturally lower than desktop due to device constraints. No critical performance or accessibility failures were present.

---

## Defensive Programming

Defensive programming and user acceptance testing were conducted across PCPartsIreland.com to ensure secure data handling, correct permissions, and reliable feature behaviour for guests, authenticated users, and admin users.

| Page | Expectation | Test | Result | Screenshot |
| --- | --- | --- | --- | --- |
| Products | Users should be able to browse all PC components without registering. | Accessed product listing and product detail pages as a guest user. | Products were fully accessible without requiring authentication. | ![screenshot](documentation/defensive/products.png) |
| Products | Products should be sortable by price and name. | Selected sorting options for price (low-to-high/high-to-low) and alphabetical order. | Sorting logic executed correctly and updated results dynamically. | ![screenshot](documentation/defensive/sorting.png) |
| Products | Products should be filterable by category. | Applied category filters (e.g. GPUs, CPUs, RAM). | Only relevant products were displayed based on selected category. | ![screenshot](documentation/defensive/filtering.png) |
| Products | Product detail pages should display complete information. | Clicked into individual product pages. | Product name, price, image, description, and add-to-cart functionality displayed correctly. | ![screenshot](documentation/defensive/product-details.png) |
| Shopping Cart | Customers should be able to add products with adjustable quantities. | Added items and increased/decreased quantities. | Cart updated correctly and recalculated totals in real time. | ![screenshot](documentation/defensive/add-to-cart.png) |
| Shopping Cart | Customers should be able to manage cart contents. | Edited quantities and removed items from cart. | Cart contents updated correctly with accurate subtotal and total calculations. | ![screenshot](documentation/defensive/manage-cart.png) |
| Checkout | Checkout page should display cart summary and secure input fields. | Proceeded to checkout with items in cart. | Cart items, grand total, and secure form inputs displayed correctly. | ![screenshot](documentation/defensive/checkout.png) |
| Checkout | Stripe payment should process securely. | Entered valid Stripe test card details and submitted payment. | Payment processed successfully and redirected to confirmation page. | ![screenshot](documentation/defensive/stripe-payment.png) |
| Checkout | Confirmation email should be sent after successful order. | Completed purchase and checked registered email inbox. | Confirmation email received containing full order summary. | ![screenshot](documentation/defensive/confirmation-email.png) |
| Checkout | Order confirmation page should display unique order number. | Completed checkout process. | Checkout success page displayed correct order number and summary. | ![screenshot](documentation/defensive/order-confirmation.png) |
| Account Management | Returning customers should be able to view order history. | Logged in and accessed profile/order history page. | Past orders were displayed accurately with full details. | ![screenshot](documentation/defensive/order-history.png) |
| Account Management | Returning customers’ shipping details should be remembered. | Completed multiple purchases while logged in. | Shipping information was pre-filled correctly on future checkouts. | ![screenshot](documentation/defensive/saved-address.png) |
| Admin Features | Admin users should be able to create new products. | Logged in as admin and created new PC component. | Product successfully saved and displayed on storefront. | ![screenshot](documentation/defensive/create-product.png) |
| Admin Features | Admin users should be able to update product details. | Edited product name, price, description, and category. | Updates saved correctly and reflected immediately on site. | ![screenshot](documentation/defensive/update-product.png) |
| Admin Features | Admin users should be able to delete products securely. | Deleted a product via admin interface. | Product removed after confirmation and no longer visible in listings. | ![screenshot](documentation/defensive/delete-product.png) |
| Orders | Admin should be able to view all placed orders. | Accessed order dashboard as admin. | All customer orders displayed correctly. | ![screenshot](documentation/defensive/view-orders.png) |
| Newsletter | Users should be able to subscribe to the newsletter. | Submitted valid email addresses. | Email addresses stored successfully. | ![screenshot](documentation/defensive/newsletter.png) |
| 404 Error Page | Invalid URLs should display a custom 404 page. | Navigated to non-existent URL (`/test`). | Custom 404 error page displayed correctly. | ![screenshot](documentation/defensive/404.png) |

All defensive tests behaved as expected, ensuring secure access control, accurate order processing, and reliable user interactions.

---

## User Story Testing

All implemented features were mapped directly to the defined user stories in the project README. Each story was tested in both expected (“happy path”) and edge-case scenarios.

| Target | Expectation | Outcome | Screenshot |
| --- | --- | --- | --- |
| As a guest user | I would like to browse products without needing to register | so that I can shop freely before deciding to create an account. | ![screenshot](documentation/features/feature01.png) |
| As a guest user | I would like to be prompted to create an account or log in at checkout | so that I can complete my purchase and track my order history. | ![screenshot](documentation/features/feature02.png) |
| As a user | I would like to sign up to the site's newsletter | so that I can stay up to date with promotions on PC components. | ![screenshot](documentation/features/feature03.png) |
| As a customer | I would like to browse product categories (GPUs, CPUs, RAM, Storage, etc.) | so that I can easily find the PC part I need. | ![screenshot](documentation/features/feature04.png) |
| As a customer | I would like to sort products by price and name | so that I can quickly compare hardware options. | ![screenshot](documentation/features/feature05.png) |
| As a customer | I would like to filter products by category | so that I can narrow down relevant PC components. | ![screenshot](documentation/features/feature06.png) |
| As a customer | I would like to view detailed product information | so that I can make an informed purchasing decision. | ![screenshot](documentation/features/feature07.png) |
| As a customer | I would like to adjust product quantities before checkout | so that I can control my order precisely. | ![screenshot](documentation/features/feature08.png) |
| As a customer | I would like to manage my shopping cart | so that I can review my selected items. | ![screenshot](documentation/features/feature09.png) |
| As a customer | I would like to remove unwanted items from my cart | so that I only purchase what I need. | ![screenshot](documentation/features/feature11.png) |
| As a customer | I would like to securely complete checkout | so that I can safely pay for my PC parts. | ![screenshot](documentation/features/feature12.png) |
| As a customer | I would like to receive an email confirmation | so that I have proof of my purchase. | ![screenshot](documentation/features/feature13.png) |
| As a customer | I would like to see a checkout success page | so that I know my order was placed successfully. | ![screenshot](documentation/features/feature14.png) |
| As a returning customer | I would like to view my previous orders | so that I can track my purchases. | ![screenshot](documentation/features/feature16.png) |
| As a site owner | I would like to create, update, and delete products | so that I can manage PCPartsIreland inventory effectively. | ![screenshot](documentation/features/feature18.png) |
| As a site owner | I would like to view all customer orders | so that I can manage fulfillment. | ![screenshot](documentation/features/feature21.png) |
| As a user | I would like to see a 404 error page if I enter an invalid URL | so that navigation errors are handled clearly. | ![screenshot](documentation/features/feature23.png) |

All user stories were successfully implemented and verified through manual testing.

---

## Automated Testing

Automated testing was performed using Django’s built-in testing framework.

Tests were executed using:

- `python3 manage.py test`

To generate a coverage report:

- `pip3 install coverage`
- `coverage run --omit="*/site-packages/*,*/migrations/*,*/__init__.py,env.py,.env" manage.py test`
- `coverage report`
- `coverage html`

Coverage report screenshot:

![screenshot](documentation/automation/html-coverage.png)

Unit tests verified core functionality including model behaviour, view responses, and order logic.

---

## Bugs

Bug tracking was managed using GitHub Issues:

https://www.github.com/colmwoods/PCPartsIreland/issues

Closed bugs:
https://www.github.com/colmwoods/PCPartsIreland/issues?q=is%3Aissue+is%3Aclosed+label%3Abug

![screenshot](documentation/bugs/gh-issues-closed.png)

Open bugs:
https://www.github.com/colmwoods/PCPartsIreland/issues?q=is%3Aissue+is%3Aopen+label%3Abug

![screenshot](documentation/bugs/gh-issues-open.png)

### Known Issues

| Issue | Screenshot |
| --- | --- |
| Project responsive from 375px upwards. Minor layout inconsistencies may occur on ultra-wide displays outside course scope. | ![screenshot](documentation/issues/poor-responsiveness.png) |
| HTML validator warning regarding `<section>` header usage. | ![screenshot](documentation/issues/section-header.png) |
| Validation warnings on `signup.html` from Django Allauth. | ![screenshot](documentation/issues/allauth.png) |
| Checkout success page accessible via known order number. | ![screenshot](documentation/issues/checkout-success.png) |
| Session storage error if product deleted while in cart. | ![screenshot](documentation/issues/session-storage.png) |
| Quantity buttons inconsistent on bag page. | ![screenshot](documentation/issues/quantity-buttons.png) |

> There are no remaining critical bugs known at the time of submission.