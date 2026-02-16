# [PCPartsIreland](https://pcpartsireland.com)

Developer: Colm Woods ([colmwoods](https://www.github.com/colmwoods))

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/colmwoods/PCPartsIreland)](https://www.github.com/colmwoods/PCPartsIreland/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/colmwoods/PCPartsIreland)](https://www.github.com/colmwoods/PCPartsIreland/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/colmwoods/PCPartsIreland)](https://www.github.com/colmwoods/PCPartsIreland)
[![badge](https://img.shields.io/badge/deployment-Heroku-purple)](https://pcpartsireland.com)

# Table of Contents
- [Project Introduction & Rationale](#project-introduction--rationale)
- [UX](#ux)
  - [The 5 Planes of UX](#the-5-planes-of-ux)
  - [1. Strategy](#1-strategy)
  - [2. Scope](#2-scope)
  - [3. Structure](#3-structure)
  - [4. Skeleton](#4-skeleton)
  - [5. Surface](#5-surface)
- [Colour Scheme](#colour-scheme)
- [Typography](#typography)
- [Wireframes](#wireframes)
- [User Stories](#user-stories)
- [Features](#features)
- [Database Design](#database-design)
- [Agile Development Process](#agile-development-process)
- [Ecommerce Business Model](#ecommerce-business-model)
- [SEO & Marketing](#seo--marketing)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

---

## Project Introduction & Rationale

**PCPartsIreland** is a full-stack e-commerce web application designed to provide customers in Ireland with a streamlined platform to browse and purchase computer components and PC hardware online. The site enables users to explore products by category, filter and sort listings, view detailed specifications, securely complete purchases using Stripe, and manage their accounts and order history.

The primary target audience includes:

- PC builders and gaming enthusiasts  
- Students and professionals upgrading hardware  
- Customers seeking reliable access to computer components within Ireland  
- First-time PC builders who benefit from clearly structured product categories  

The application focuses on delivering a smooth, intuitive user experience while maintaining strong administrative control for the site owner. Administrators can create, update, and delete products, manage categories, review orders, and oversee site content such as FAQs and newsletter subscriptions. This ensures the platform remains scalable, maintainable, and aligned with business needs.

### Why This Project?

I chose to build **PCPartsIreland** because of my strong personal interest in computers, hardware, and system building. Having built and upgraded PCs myself, I understand the challenges customers face when searching for compatible components. Many existing sites feel cluttered, overly complex, or are not tailored specifically to an Irish audience.

This project allowed me to:

- Combine technical development skills with a subject I am genuinely passionate about  
- Design structured product categorisation that reflects real-world hardware organisation  
- Apply full-stack Django development principles in a realistic business scenario  
- Implement secure Stripe payment processing and order management systems  
- Demonstrate database relationships, authentication, CRUD functionality, and deployment practices  

From an academic perspective, this project demonstrates:

- Full e-commerce functionality  
- Secure Stripe integration  
- Custom Django models  
- Role-based permissions  
- Database design and ERD modelling  
- Agile project management via GitHub Projects  
- Deployment using Heroku and PostgreSQL  

PCPartsIreland is therefore not just an online shop, but a complete demonstration of my ability to design, build, deploy, and document a production-ready full-stack web application.

![screenshot](documentation/mockup.jpg)

source: [PCPartsIreland amiresponsive](https://ui.dev/amiresponsive?url=https://pcpartsireland.com)

---

## UX

### The 5 Planes of UX
#### 1. Strategy

**Purpose**
- Provide a seamless and intuitive e-commerce experience for customers to browse, filter, and purchase products.
- Empower site owners to manage the store's inventory and customer orders efficiently.

**Primary User Needs**
- Guest users need to browse products and checkout with ease.
- Registered customers need a streamlined shopping experience with account and order history features.
- Site owners need robust tools for inventory and order management.

**Business Goals**
- Drive sales by providing a user-friendly shopping experience.
- Build customer loyalty through personalized and efficient account features.
- Maintain an organized and up-to-date store inventory.

#### 2. Scope

**[Features](#features)** (see below)

**Content Requirements**
- Product details, including name, price, description, category, and images.
- Clear prompts and instructions for browsing, filtering, and purchasing.
- Order details, confirmation pages, and email notifications.
- Secure payment processing using Stripe.
- Payment success emails sent to users.
- 404 page for lost users.

#### 3. Structure

**Information Architecture**
- **Navigation Menu**:
  - Links to Home, Products, Cart, Newsletter, and Account sections.
- **Hierarchy**:
  - Prominent product categories and filters for easy navigation.
  - Cart and checkout options displayed prominently for convenience.

**User Flow**
1. Guest user browses the store → filters and sorts products by category, price, or name.
2. Guest user adds items to the cart → proceeds to checkout.
3. Guest user creates an account or logs in during checkout → completes purchase.
4. Returning customers log in → view past orders and track purchase history.
5. Site owners manage inventory → add, update, or delete products and categories.
6. Users signup to the newsletter → potentially receive advanced notice of upcoming sales.

#### 4. Skeleton

**[Wireframes](#wireframes)** (see below)

#### 5. Surface

**Visual Design Elements**
- **[Colours](#colour-scheme)** (see below)
- **[Typography](#typography)** (see below)

### Colour Scheme

I used [coolors.co](https://coolors.co/080708-3772ff-df2935-fdca40-e6e8e6) to generate my color palette.

- `#000000` Primary structural colour (buttons, emphasis, layout).
- `#111111` Header / dark background.
- `#FFFFFF` Text and contrast.
- `#FF6600` Main call-to-action (Shop Now, key buttons).
- `#E65C00` CTA hover state.

![screenshot](documentation/coolors.jpg)

### Typography

- [Montserrat](https://fonts.google.com/specimen/Montserrat) was used for the primary headers and titles.
- [Lato](https://fonts.google.com/specimen/Lato) was used for all other secondary text.
- [Font Awesome](https://fontawesome.com) icons were used throughout the site, such as the social media icons in the footer.

## Wireframes

To follow best practice, wireframes were developed for mobile, tablet, and desktop sizes.
I've used [Balsamiq](https://balsamiq.com/wireframes) to design my site wireframes.

| Page | Mobile | Tablet | Desktop |
| --- | --- | --- | --- |
| Register | ![screenshot](documentation/wireframes/mobile-register.jpg) | ![screenshot](documentation/wireframes/tablet-register.jpg) | ![screenshot](documentation/wireframes/desktop-register.jpg) |
| Login | ![screenshot](documentation/wireframes/mobile-login.jpg) | ![screenshot](documentation/wireframes/tablet-login.jpg) | ![screenshot](documentation/wireframes/desktop-login.jpg) |
| Change Password | ![screenshot](documentation/wireframes/mobile-password.jpg) | ![screenshot](documentation/wireframes/tablet-password.jpg) | ![screenshot](documentation/wireframes/desktop-password.jpg) |
| Profile | ![screenshot](documentation/wireframes/mobile-profile.jpg) | ![screenshot](documentation/wireframes/tablet-profile.jpg) | ![screenshot](documentation/wireframes/desktop-profile.jpg) |
| Home | ![screenshot](documentation/wireframes/mobile-home.jpg) | ![screenshot](documentation/wireframes/tablet-home.jpg) | ![screenshot](documentation/wireframes/desktop-home.jpg) |
| Products | ![screenshot](documentation/wireframes/mobile-products.jpg) | ![screenshot](documentation/wireframes/tablet-products.jpg) | ![screenshot](documentation/wireframes/desktop-products.jpg) |
| Product Details | ![screenshot](documentation/wireframes/mobile-product-details.jpg) | ![screenshot](documentation/wireframes/tablet-product-details.jpg) | ![screenshot](documentation/wireframes/desktop-product-details.jpg) |
| Bag | ![screenshot](documentation/wireframes/mobile-bag.jpg) | ![screenshot](documentation/wireframes/tablet-bag.jpg) | ![screenshot](documentation/wireframes/desktop-bag.jpg) |
| Checkout | ![screenshot](documentation/wireframes/mobile-checkout.jpg) | ![screenshot](documentation/wireframes/tablet-checkout.jpg) | ![screenshot](documentation/wireframes/desktop-checkout.jpg) |
| Checkout Success | ![screenshot](documentation/wireframes/mobile-checkout-success.jpg) | ![screenshot](documentation/wireframes/tablet-checkout-success.jpg) | ![screenshot](documentation/wireframes/desktop-checkout-success.jpg) |
| Add Product | ![screenshot](documentation/wireframes/mobile-add-product.jpg) | ![screenshot](documentation/wireframes/tablet-add-product.jpg) | ![screenshot](documentation/wireframes/desktop-add-product.jpg) |
| Edit Product | ![screenshot](documentation/wireframes/mobile-edit-product.jpg) | ![screenshot](documentation/wireframes/tablet-edit-product.jpg) | ![screenshot](documentation/wireframes/desktop-edit-product.jpg) |
| Newsletter | ![screenshot](documentation/wireframes/mobile-newsletter.jpg) | ![screenshot](documentation/wireframes/tablet-newsletter.jpg) | ![screenshot](documentation/wireframes/desktop-newsletter.jpg) |
| Contact | ![screenshot](documentation/wireframes/mobile-contact.jpg) | ![screenshot](documentation/wireframes/tablet-contact.jpg) | ![screenshot](documentation/wireframes/desktop-contact.jpg) |
| 404 | ![screenshot](documentation/wireframes/mobile-404.jpg) | ![screenshot](documentation/wireframes/tablet-404.jpg) | ![screenshot](documentation/wireframes/desktop-404.jpg) |

## User Stories

| Target | Expectation | Outcome |
| --- | --- | --- |
| As a guest user | I would like to browse PC components without needing to register | so that I can explore products before committing to an account. |
| As a guest user | I would like to be prompted to create an account or log in at checkout | so that I can complete my purchase and track my order history. |
| As a user | I would like to sign up to the site's newsletter | so that I can stay up to date with hardware releases, restocks, and promotions. |
| As a customer | I would like to browse various hardware categories (CPU, GPU, RAM, Storage, Prebuilt PCs, Accessories) | so that I can easily find what I need. |
| As a customer | I would like to use the search bar to find specific components | so that I can quickly locate a product by name or keyword. |
| As a customer | I would like to sort products by price and name | so that I can compare hardware within my budget. |
| As a customer | I would like to filter products by category | so that I can narrow down hardware types efficiently. |
| As a customer | I would like to view detailed specifications on each product page | so that I can make informed compatibility decisions. |
| As a customer | I would like to see whether a product is in stock | so that I know if it can be purchased immediately. |
| As a customer | I would like to know the maximum quantity available | so that I cannot order more units than are in stock. |
| As a customer | I would like to increase or decrease product quantity before adding to cart | so that I can control how many units I purchase. |
| As a customer | I would like to be prevented from checking out if stock is insufficient | so that I cannot complete an invalid order. |
| As a customer | I would like to view and manage my shopping cart | so that I can review, adjust, or remove components. |
| As a customer | I would like to proceed to checkout with a clear breakdown of items and totals | so that I understand my purchase fully. |
| As a customer | I would like to securely enter my card details using Stripe | so that my payment information is protected. |
| As a customer | I would like to receive a confirmation email after my purchase | so that I have a record of my transaction. |
| As a customer | I would like to see a checkout success page with an order number | so that I know my order was successful. |
| As a returning customer | I would like to log in and view past orders | so that I can track previous purchases. |
| As a returning customer | I would like my shipping details remembered | so that future checkouts are faster. |
| As a site owner | I would like to create new products with name, description, price, images, category, and stock quantity | so that inventory is properly managed. |
| As a site owner | I would like to update product details and stock levels | so that listings remain accurate. |
| As a site owner | I would like stock to automatically reduce after purchase | so that inventory reflects real-time sales. |
| As a site owner | I would like to delete discontinued products | so that customers cannot purchase unavailable hardware. |
| As a site owner | I would like to view all orders placed | so that I can manage fulfilment and revenue tracking. |
| As a site owner | I would like to manage product categories | so that hardware remains logically structured. |
| As a user | I would like to see a custom 404 page if I get lost | so that it is clear the page does not exist. |

---

## Features

### Existing Features

| Feature | Notes | Screenshot |
| --- | --- | --- |
| Register | Authentication is handled by Django Allauth, allowing secure user registration and account creation. | ![screenshot](documentation/features/register.jpg) |
| Login | Registered users can securely log in to manage their account and order history. | ![screenshot](documentation/features/login.jpg) |
| Logout | Users can safely log out of their account to protect personal data. | ![screenshot](documentation/features/logout.jpg) |
| Product List | Displays all available PC components in a structured grid layout. Includes sorting, filtering, and search functionality. | ![screenshot](documentation/features/product-list.jpg) |
| Search Bar | A navigation-based search bar allows users to search for hardware by keyword or product name. | ![screenshot](documentation/features/search-bar.jpg) |
| Sorting & Filtering | Products can be sorted by price or name and filtered by category for easier browsing. | ![screenshot](documentation/features/product-list.jpg) |
| Product Details | Shows product specifications, description, pricing, imagery, and stock-aware quantity controls. | ![screenshot](documentation/features/product-details.jpg) |
| Stock Management | Quantity controls prevent users from selecting more units than are available in stock. | ![screenshot](documentation/features/product-details.jpg) |
| Add to Bag | Users can add selected quantities of hardware to their shopping cart. | ![screenshot](documentation/features/add-to-bag.jpg) |
| View Bag | Users can review cart contents, update quantities, remove products, and view updated totals. | ![screenshot](documentation/features/view-bag.jpg) |
| Checkout | Stripe integration provides secure payment processing and order validation. | ![screenshot](documentation/features/checkout.jpg) |
| Order Confirmation | Users receive both on-screen and email confirmation with full order breakdown. | ![screenshot](documentation/features/order-confirmation.jpg) |
| Profile Management | Users can manage personal details and store default shipping information. | ![screenshot](documentation/features/profile-management.jpg) |
| Order History | Logged-in users can view past orders and purchase details. | ![screenshot](documentation/features/order-history.jpg) |
| Product Management | Superusers can add, edit, update stock, and delete products via a full CRUD interface. | ![screenshot](documentation/features/product-management.jpg) |
| Newsletter | Users can subscribe to receive updates on hardware releases and promotions. | ![screenshot](documentation/features/newsletter.jpg) |
| Contact | Contact form stores user enquiries in the database for admin review. | ![screenshot](documentation/features/contact.jpg) |
| FAQs | Admin-managed FAQ section provides answers to common purchasing queries. | ![screenshot](documentation/features/faqs.jpg) |
| User Feedback | Django messaging framework provides real-time feedback (e.g., added to cart, removed item, insufficient stock). | ![screenshot](documentation/features/user-feedback.jpg) |
| SEO | Includes sitemap.xml, robots.txt, and optimised metadata. | ![screenshot](documentation/features/seo.jpg) |
| Marketing | Footer includes social media integration to support brand growth. | ![screenshot](documentation/features/marketing.jpg) |
| Heroku Deployment | The site is deployed and publicly accessible via Heroku. | ![screenshot](documentation/features/heroku.jpg) |
| 404 | Custom branded 404 page replaces the default server error page. | ![screenshot](documentation/features/404.jpg) |
| 500 | Custom branded 500 page replaces the default server error 500 page. | ![screenshot](documentation/features/500.jpg) |

---

### Future Features

The following features represent planned improvements for PCPartsIreland. These enhancements aim to improve user experience, increase customer retention, and strengthen the platform’s competitiveness within the PC hardware market.

- **Product Reviews & Ratings**:  
  Allow customers to leave reviews and rate products, with admin moderation to prevent spam or abuse. Average ratings and total review counts would be displayed on product pages to build trust and help customers make informed decisions when purchasing hardware.

- **Wishlist Functionality**:  
  Enable users to save products to a personal wishlist for future purchases or planned PC builds. Users could receive notifications if wishlist items go on sale or return to stock, increasing return visits and engagement.

- **Product Recommendations**:  
  Implement a “Customers who bought this also bought” or “You might also like” feature. This would be particularly useful for suggesting compatible components such as RAM for a motherboard or a PSU suitable for a selected GPU.

- **Live Chat Support**:  
  Provide real-time customer support through an integrated live chat or chatbot system. This would help customers with compatibility questions, stock queries, and general purchasing advice.

- **Abandoned Cart Recovery**:  
  Automatically send reminder emails to users who add items to their cart but do not complete checkout. This could include optional discount incentives to improve conversion rates.

- **Discount Codes and Vouchers**:  
  Allow administrators to create promotional discount codes for seasonal sales, hardware launches, or clearance events. This supports marketing campaigns and increases sales during peak periods.

- **Loyalty Program**:  
  Introduce a points-based loyalty system where customers earn points for purchases and redeem them for discounts. This encourages repeat business and long-term customer retention.

- **Product Inventory Alerts**:  
  Notify customers when out-of-stock items are back in stock, and optionally alert administrators when inventory levels fall below a certain threshold to improve stock management.

- **Multi-Currency and Multi-Language Support**:  
  Expand the platform to support additional currencies and languages, enabling potential growth beyond the Irish market.

- **Product Bundles**:  
  Offer discounted hardware bundles (e.g., CPU + motherboard + RAM kits) or complete upgrade packages. This simplifies purchasing decisions and increases average order value.

- **Social Media Integration**:  
  Enable users to share products directly to social media platforms and potentially support social login functionality for faster account creation.

- **Shipping Tracking Integration**:  
  Provide real-time courier tracking information within the user’s order history, improving transparency and reducing customer support enquiries.

- **Advanced Analytics Dashboard for Admin**:  
  Develop a comprehensive dashboard showing sales trends, best-selling products, category performance, and customer purchasing behaviour to support data-driven business decisions.

- **Subscription-Based Products**:  
  Allow users to subscribe to certain consumable products (e.g., thermal paste, cleaning kits, peripherals) for recurring deliveries.

- **Product Video Demos**:  
  Support embedded product videos, such as GPU benchmarks or CPU performance demonstrations, to better showcase high-performance components.

- **Mobile App**:  
  Develop a mobile application for iOS and Android to provide a more optimised shopping experience, push notifications for deals, and saved build configurations.

- **PC Compatibility Checker**:  
  Introduce a system that automatically checks compatibility between selected components (CPU socket, RAM type, GPU clearance, PSU wattage) to reduce incorrect purchases.

- **PC Builder Tool (PCPartPicker-Style)**:  
  Implement a guided PC builder that allows users to assemble a full system step-by-step with live pricing updates and compatibility validation.

- **Hardware Comparison Tool**:  
  Allow side-by-side comparison of specifications such as CPU cores, GPU VRAM, RAM speed, and storage type to assist customers in making technical decisions.

---

## Tools & Technologies

| Tool / Tech | Use |
| --- | --- |
| [![badge](https://img.shields.io/badge/Markdown_Builder-grey?logo=markdown&logoColor=000000)](https://markdown.2bn.dev) | Generate README and TESTING templates. |
| [![badge](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) | Version control. (`git add`, `git commit`, `git push`) |
| [![badge](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) | Secure online code storage. |
| [![badge](https://img.shields.io/badge/VSCode-grey?logo=htmx&logoColor=007ACC)](https://code.visualstudio.com) | Local IDE for development. |
| [![badge](https://img.shields.io/badge/HTML-grey?logo=html5&logoColor=E34F26)](https://en.wikipedia.org/wiki/HTML) | Main site content and layout. |
| [![badge](https://img.shields.io/badge/CSS-grey?logo=css&logoColor=1572B6)](https://en.wikipedia.org/wiki/CSS) | Design and layout. |
| [![badge](https://img.shields.io/badge/JavaScript-grey?logo=javascript&logoColor=F7DF1E)](https://www.javascript.com) | User interaction on the site. |
| [![badge](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) | Back-end programming language. |
| [![badge](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) | Hosting the deployed back-end site. |
| [![badge](https://img.shields.io/badge/Bootstrap-grey?logo=bootstrap&logoColor=7952B3)](https://getbootstrap.com) | Front-end CSS framework for modern responsiveness and pre-built components. |
| [![badge](https://img.shields.io/badge/Django-grey?logo=django&logoColor=092E20)](https://www.djangoproject.com) | Python framework for the site. |
| [![badge](https://img.shields.io/badge/PostgreSQL-grey?logo=postgresql&logoColor=4169E1)](https://www.postgresql.org) | Relational database management. |
| [![badge](https://img.shields.io/badge/WhiteNoise-grey?logo=python&logoColor=FFFFFF)](https://whitenoise.readthedocs.io) | Serving static files with Heroku. |
| [![badge](https://img.shields.io/badge/Stripe-grey?logo=stripe&logoColor=008CDD)](https://stripe.com) | Online secure payments of e-commerce products/services. |
| [![badge](https://img.shields.io/badge/Gmail_API-grey?logo=gmail&logoColor=EA4335)](https://mail.google.com) | Sending emails in my application. |
| [![badge](https://img.shields.io/badge/MailChimp-grey?logo=mailchimp&logoColor=FFE01B)](https://mailchimp.com) | Sending newsletter subscriptions. |
| [![badge](https://img.shields.io/badge/AWS_S3-grey?logo=amazons3&logoColor=569A31)](https://aws.amazon.com/s3) | Online static file storage. |
| [![badge](https://img.shields.io/badge/Figma-grey?logo=figma&logoColor=F24E1E)](https://www.figma.com) | Creating wireframes. |
| [![badge](https://img.shields.io/badge/Font_Awesome-grey?logo=fontawesome&logoColor=528DD7)](https://fontawesome.com) | Icons. |
| [![badge](https://img.shields.io/badge/ChatGPT-grey?logo=openai&logoColor=75A99C)](https://chat.openai.com) | Help debug, troubleshoot, and explain things. |
| [![badge](https://img.shields.io/badge/Mermaid-grey?logo=mermaid&logoColor=FF3670)](https://mermaid.live) | Generate an interactive diagram for the data/schema. |
| [![badge](https://img.shields.io/badge/W3Schools-grey?logo=w3schools&logoColor=04AA6D)](https://www.w3schools.com) | Tutorials/Reference Guide |
| [![badge](https://img.shields.io/badge/StackOverflow-grey?logo=stackoverflow&logoColor=F58025)](https://stackoverflow.com) | Troubleshooting and Debugging |

---

## Database Design

### Data Model

PCPartsIreland uses a relational database powered by PostgreSQL and managed through Django’s ORM. The data model was carefully structured to support e-commerce functionality, structured product organisation, inventory-aware ordering, and secure payment processing.

The core models in the system are:

User  
Handles authentication and login functionality using Django’s built-in user model.

UserProfile  
Extends the default User model using a one-to-one relationship.  
Stores default delivery information such as phone number, address, town/city, county, postcode, and country.  
This improves checkout efficiency for returning customers.

Category  
Organises products into structured hardware categories (e.g., CPUs, GPUs, RAM, Storage).  
Each category contains multiple products using a one-to-many relationship.

Product  
Stores all product-related data including:
- SKU
- Name
- Description
- Price
- Rating
- Image
- Category relationship

Each product belongs to a single category but can appear in multiple customer orders.

Order  
Represents a completed checkout transaction.  
Stores:
- Order number
- Customer details
- Delivery address
- Order totals
- Stripe payment reference
- Original cart data
- Timestamp

OrderLineItem  
Breaks down an Order into individual purchased products.  
Stores:
- Product reference
- Quantity ordered
- Line total price

This model ensures accurate quantity tracking and allows customers to order multiple units of the same product while maintaining correct stock awareness.

Newsletter  
Stores email addresses of users who subscribe to marketing updates.

Contact  
Stores contact form submissions including name, email, and message content.

FAQ  
Allows administrators to manage frequently asked questions displayed on the site.

### Relationship Overview

- One User has one UserProfile
- One Category has many Products
- One Order has many OrderLineItems
- One OrderLineItem references one Product
- Orders optionally relate to a UserProfile

This relational structure ensures:

- Accurate order tracking
- Clean separation of concerns
- Scalable product management
- Secure transaction storage
- Efficient retrieval of user purchase history

The ERD below visualises these relationships.

![screenshot](documentation/erd.jpg)

I have used `Mermaid` to generate an interactive ERD of my project.

```mermaid
erDiagram
    User {
        int id PK
        varchar username
        varchar email
        varchar password
    }

    UserProfile {
        int id PK
        varchar default_phone_number
        varchar default_street_address1
        varchar default_street_address2
        varchar default_town_or_city
        varchar default_county
        varchar default_postcode
        varchar default_country
    }

    User ||--|| UserProfile : has_one

    Category {
        int id PK
        varchar name
        varchar friendly_name
    }

    Product {
        int id PK
        varchar sku
        varchar name
        text description
        bool has_sizes
        decimal price
        decimal rating
        varchar image_url
        image image
    }

    Product ||--o| Category : belongs_to

    Order {
        int id PK
        varchar order_number
        varchar full_name
        varchar email
        varchar phone_number
        varchar country
        varchar postcode
        varchar town_or_city
        varchar street_address1
        varchar street_address2
        varchar county
        datetime date
        decimal delivery_cost
        decimal order_total
        decimal grand_total
        text original_bag
        varchar stripe_pid
    }

    OrderLineItem {
        int id PK
        int quantity
        decimal lineitem_total
        varchar product_size
    }

    Order ||--o| OrderLineItem : has_many
    OrderLineItem ||--o| Product : belongs_to

    Order ||--o| UserProfile : belongs_to

    Newsletter {
        int id PK
        varchar email
    }

    Contact {
        int id PK
        varchar name
        varchar email
        text message
    }

    FAQ {
        int id PK
        varchar question
        text answer
    }
```

source: [Mermaid](https://mermaid.live/edit#pako:eNqVVcFu2zAM_RVD57RIHLdpfRs6DBg2bB2GXYYAhmIxjlBZcimqqdvk3yfbSVPHceP5kBh8TyRFPtKvLDUCWMwAP0ueIc_nOvDPHwsYvDbv1SM1BVIE998OpieO6Ypj4DxV8xy6CORcqq654NauDYoG2c71IeQ9mqVUMDCygCV3ipJiZTQk2uULwH6WJQSghAuBYO1kKDHsJ5JZ68Rgkkoq-1mpcfojvDCWqiac8YDliXoFm83FxWbTql0crLhNfEX2xDtOkBksB1b1dC-XKEELVSYH-C0TH1m4lAb6tw_uXFCCZ_K3tynKgqTRB2RhjKrvZ-UL2INdQCpzroICZQpdM3KSOuuG9WAGicN3Kq1NzW_PNauam82hrHGwAGV0Zr0g9tyfKAYPkKm4vfJdOqWS_5uvD8ehJabWsV4dfqzzs3N1dp6OJ0T4ypLMoX7pNlOAkk-ApZ8LS124KScZ4qoL-g2nxTFYy82gzKTmKlnw7OQdZAFJIY-3Vt3o71LDV4L8TMMr06Pjmlp13KemvBPpnRxn99afRn618k8lsddlO6NmG-Rcl6fy3R3ZK7tfyTtie890yT9gbRUQDdb-Owm_3ebOaOKD18mg0ag7nHv1daf6y6dfAyM9OrDtbVS75dqu94O2ZSOWA_rgwn9Ta7dzRivwKbLYvwqOD3M21xWPOzK_S52ymNDBiLmikvvuK8ziJVfWWwuuWfzKnlk8jSaXN9ez8HoyHc_C8TiajVjJ4ovp5XUUTqMovLqdXd2Et-FsO2Ivxngfk8vxZBpGkT_m_zxW-_tbY01QNC5b7YJt_wE0ZoQj)

I have used `pygraphviz` and `django-extensions` to auto-generate an ERD.

The steps taken were as follows:
- In the terminal: `sudo apt update`
- then: `sudo apt-get install python3-dev graphviz libgraphviz-dev pkg-config`
- then type `Y` to proceed
- then: `pip3 install django-extensions pygraphviz`
- in my `settings.py` file, I added the following to my `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    ...
    'django_extensions',
    ...
]
```
- back in the terminal: `python3 manage.py graph_models -a -o erd.jpg`
- drag the new `erd.jpg` file into my `documentation/` folder
- removed `'django_extensions',` from my `INSTALLED_APPS`
- finally, in the terminal: `pip3 uninstall django-extensions pygraphviz -y`

![screenshot](documentation/advanced-erd.jpg)

source: [medium.com](https://medium.com/@yathomasi1/1-using-django-extensions-to-visualize-the-database-diagram-in-django-application-c5fa7e710e16)

## Agile Development Process

### GitHub Projects

[GitHub Projects](https://www.github.com/colmwoods/PCPartsIreland/projects) served as the primary Agile planning tool throughout the development of PCPartsIreland.

EPICs were first defined at a high level (e.g., Product Management, Checkout & Payments, User Authentication, Inventory & Orders). These EPICs were then broken down into detailed User Stories and implemented incrementally.

A Kanban-style project board was used to move tasks through development stages such as:

- Backlog  
- To Do  
- In Progress  
- Testing  
- Done  

This structured workflow ensured:

- Clear feature planning  
- Logical development progression  
- Transparent milestone tracking  
- Efficient bug management  

![screenshot](documentation/gh-projects.jpg)


### GitHub Issues

[GitHub Issues](https://www.github.com/colmwoods/PCPartsIreland/issues) were used to manage User Stories, bugs, and feature implementation tasks.

Each issue included:

- A detailed description of functionality
- Defined acceptance criteria
- MoSCoW prioritisation labels
- References to related commits where applicable

This ensured traceability between planning and implementation, aligning development with Agile principles.

| Link | Screenshot |
| --- | --- |
| [![GitHub issues](https://img.shields.io/github/issues-search/colmwoods/PCPartsIreland?query=is%3Aissue%20is%3Aopen%20-label%3Abug&label=Open%20Issues&color=yellow)](https://www.github.com/colmwoods/PCPartsIreland/issues?q=is%3Aissue%20is%3Aopen%20-label%3Abug) | ![screenshot](documentation/gh-issues-open.jpg) |
| [![GitHub closed issues](https://img.shields.io/github/issues-search/colmwoods/PCPartsIreland?query=is%3Aissue%20is%3Aclosed%20-label%3Abug&label=Closed%20Issues&color=green)](https://www.github.com/colmwoods/PCPartsIreland/issues?q=is%3Aissue%20is%3Aclosed%20-label%3Abug) | ![screenshot](documentation/gh-issues-closed.jpg) |


### MoSCoW Prioritization

I've decomposed my EPICs into User Stories for prioritizing and implementing them. Using this approach, I was able to apply MoSCoW prioritization and labels to my User Stories within the Issues tab.

- **Must Have**: guaranteed to be delivered - required to pass the project (max ~60% of stories). These included core e-commerce functionality such as product listing, search and filtering, stock-aware ordering, cart management, checkout, Stripe payments, and order confirmation.

- **Should Have**: adds significant value, but not vital (~20% of stories). These included usability improvements, enhanced filtering, improved UI feedback, and profile enhancements.

- **Could Have**: has small impact if left out (the remaining ~20% of stories). These included additional refinements and minor UX improvements.

- **Won't Have**: not a priority for this iteration - future features such as a PC compatibility checker, full PC builder tool, advanced analytics dashboard, and loyalty system.

---


## Ecommerce Business Model

PCPartsIreland sells PC hardware components directly to individual customers, and therefore follows a **Business to Customer (B2C)** model. It operates using a straightforward transactional structure, where customers browse products, add items to their cart, and complete purchases securely online. It does not currently rely on subscription services or recurring payment models.

The platform is still in its early development stages, although it already includes newsletter functionality and social media integration to support marketing efforts.

Social media can help build a community around PCPartsIreland, increase visibility within the Irish tech and gaming market, and drive additional site traffic — particularly when using widely adopted platforms such as Facebook.

The newsletter allows the business to communicate directly with customers. This can include notifications about special offers, new hardware releases, restocked components, updates to delivery options, changes to business hours, and other relevant announcements.

## SEO & Marketing

### Keywords

I've identified appropriate keywords that align with PCPartsIreland, helping users find the site more easily through search engines. This included a combination of:

- Short-tail (head terms) keywords
- Long-tail keywords

Examples include terms such as “PC parts Ireland”, “gaming GPU Ireland”, “DDR5 RAM Ireland”, and more specific searches like “buy RTX graphics card Ireland delivery”.

I've also used [Word Tracker](https://www.wordtracker.com) to review search frequency and competitiveness of some of the site's primary keywords (during the free trial period).

### Sitemap

I've used [XML-Sitemaps](https://www.xml-sitemaps.com) to generate a sitemap.xml file. This was generated using the deployed site URL: https://pcpartsireland.com

After crawling the entire site, it created a [sitemap.xml](sitemap.xml), which I downloaded and included in the repository to improve search engine indexing.

### Robots

I've created the [robots.txt](robots.txt) file at the root-level. Inside, I've included the default settings:

User-agent: *
Disallow:
Sitemap: https://pcpartsireland.com/sitemap.xml

Further links for future implementation:
- [Google search console](https://search.google.com/search-console)
- [Creating and submitting a sitemap](https://developers.google.com/search/docs/advanced/sitemaps/build-sitemap)
- [Managing your sitemaps and using sitemaps reports](https://support.google.com/webmasters/answer/7451001)
- [Testing the robots.txt file](https://support.google.com/webmasters/answer/6062598)

### Social Media Marketing

Creating a strong social presence and linking it to the PCPartsIreland website can help drive engagement and increase sales. Using widely adopted platforms such as Facebook helps maximise exposure within the Irish tech and gaming community.

I've created a mockup Facebook business account using the [Balsamiq template](https://code-institute-org.github.io/5P-Assessments-Handbook/files/Facebook_Mockups.zip) provided by Code Institute.

![screenshot](documentation/mockup-facebook.jpg)

### Newsletter Marketing

I have incorporated newsletter functionality within the application to allow users to supply their email address if they are interested in receiving updates about PCPartsIreland products and promotions.

Two newsletter approaches are supported:

**1. Custom Django Model Newsletter**

- A custom `newsletter` app was created within the project, containing a model called `Newsletter`.
- This satisfies two assessment criteria:
    1. Including a newsletter feature
    2. Implementing one of the required custom models
- The model stores subscriber email addresses securely.
- The existing `send_mail()` functionality used within `webhook_handler.py` can be reused to send promotional emails when new products are added to the store.

**2. MailChimp Newsletter (Alternative Option)**

- A Mailchimp account can be created to manage campaigns externally.
- This allows up to 2,500 subscription email sends per month.
- Mailchimp scripts can be integrated into the project following Code Institute guidance.

Example Mailchimp embedded form integration:

<script>
document.getElementById("mc-embedded-subscribe-form").addEventListener("submit", function(e) {
    const emailInput = document.getElementById("mce-EMAIL").value;
    if (!emailInput.includes("@")) {
        e.preventDefault();
        alert("Please enter a valid email address.");
    }
});
</script>

This JavaScript provides simple client-side validation before submitting the form to Mailchimp.

## Testing

> [!NOTE]  
> For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

The live deployed application can be found on [Heroku](https://pcpartsireland.com).

## Security Considerations

- All secret keys are stored in environment variables and never committed to the repository.
- DEBUG is set to False in production.
- Sensitive files such as env.py are included in .gitignore.
- Stripe webhook signing is verified before processing events.


### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications in the cloud.

Deployment steps after account setup:

- Select **New** in the top-right corner of the Heroku Dashboard and choose **Create new app**.
- Ensure the app name is unique and select the closest region (EU or USA), then click **Create App**.
- From the app **Settings**, click **Reveal Config Vars**, and configure environment variables to match your private `env.py` file.

| Key | Value |
| --- | --- |
| `AWS_ACCESS_KEY_ID` | user-inserts-own-aws-access-key-id |
| `AWS_SECRET_ACCESS_KEY` | user-inserts-own-aws-secret-access-key |
| `DATABASE_URL` | user-inserts-own-postgres-database-url |
| `DISABLE_COLLECTSTATIC` | 1 (*temporary during setup*) |
| `EMAIL_HOST_PASS` | user-inserts-own-gmail-api-key |
| `EMAIL_HOST_USER` | user-inserts-own-gmail-email-address |
| `SECRET_KEY` | any-random-secret-key |
| `STRIPE_PUBLIC_KEY` | user-inserts-own-stripe-public-key |
| `STRIPE_SECRET_KEY` | user-inserts-own-stripe-secret-key |
| `STRIPE_WH_SECRET` | user-inserts-own-stripe-webhook-secret |
| `USE_AWS` | True |

Heroku requires the following additional files:

- [requirements.txt](requirements.txt)
- [Procfile](Procfile)
- [.python-version](.python-version)


You can install this project's **[requirements.txt](requirements.txt)** (where applicable) using:

- `pip3 install -r requirements.txt`

If you install additional packages while developing or extending PCPartsIreland, the requirements file should be updated using:

- `pip3 freeze --local > requirements.txt`

The **[Procfile](Procfile)** can be created with the following command:

- `echo web: gunicorn app_name.wsgi > Procfile`
- Replace `app_name` with the name of your primary Django project folder (the folder containing `settings.py`).

The **[.python-version](.python-version)** file tells Heroku which Python version to use when running PCPartsIreland.

- `3.12` (or similar)

For Heroku deployment, follow these steps to connect your GitHub repository to the newly created app:

Either (recommended):

- Select **Automatic Deployment** from the Heroku app dashboard.

Or:

- In the Terminal/CLI, connect to Heroku using:
  - `heroku login -i`
- Set the Heroku remote:
  - `heroku git:remote -a app_name` (replace `app_name` with your Heroku app name)
- After completing the standard Git `add`, `commit`, and `push` to GitHub, deploy using:
  - `git push heroku main`

The PCPartsIreland project should now be connected and deployed to Heroku.

### PostgreSQL

This project uses a [Code Institute PostgreSQL Database](https://dbs.ci-dbs.net) as its relational database.

- PostgreSQL databases provided by Code Institute are only available to CI students.
- If cloning or forking this repository outside Code Institute, you will need to configure your own PostgreSQL database.
- Code Institute students are allowed a maximum of 8 databases.
- Databases may be subject to deletion after 18 months.

To obtain a PostgreSQL database from Code Institute:

- Submit your email address using the link above.
- An email will be sent containing your database credentials.
- The connection string will resemble:
  - `postgres://<db_username>:<db_password>@<db_host_url>/<db_name>`
- This connection string should be added to your `env.py` file and Heroku Config Vars as `DATABASE_URL`.

### Stripe API

This project uses [Stripe](https://stripe.com) to handle e-commerce payments for PCPartsIreland.

After creating a Stripe account:

- From the Stripe dashboard, expand “Get your test API keys”.
- Two keys will be available:
  - `STRIPE_PUBLIC_KEY` (Publishable Key, starts with **pk**)
  - `STRIPE_SECRET_KEY` (Secret Key, starts with **sk**)

To add Stripe Webhooks:

- In the Stripe dashboard, go to **Developers** → **Webhooks**.
- Click **Add Endpoint**.
  - `https://pcpartsireland.com/checkout/wh/`
- Select **receive all events**.
- Click **Add Endpoint**.
- Stripe will generate:
  - `STRIPE_WH_SECRET` (Webhook Signing Secret, starts with **wh**)

### Gmail API

This project uses [Gmail](https://mail.google.com) to send order confirmation emails to customers of PCPartsIreland.

To configure Gmail:

- Open Gmail and click the **Account Settings** (cog icon).
- Select **Accounts and Import**.
- Under “Change account settings”, click **Other Google Account settings**.
- Select **Security**.
- Enable **2-Step Verification**.
- After enabling 2FA, return to **Security**.
- Select **App passwords**.
- Choose:
  - App: **Mail**
  - Device: **Other (Custom name)** (e.g., “PCPartsIreland”)
- A 16-character password (API key) will be generated.
  - Save it securely.
  - Remove any spaces if present.
  - Set:
    - `EMAIL_HOST_PASS` to the 16-character key
    - `EMAIL_HOST_USER` to your Gmail address

### WhiteNoise

This project uses [WhiteNoise](https://whitenoise.readthedocs.io/en/latest/) to serve static files on the deployed Heroku version of PCPartsIreland.

To configure WhiteNoise:

- Install the package:
  - `pip install whitenoise`
- Update requirements:
  - `pip freeze --local > requirements.txt`
- Add WhiteNoise to `settings.py` above other middleware (except SecurityMiddleware):

```python
# settings.py

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # any additional middleware
]
```

### Local Development

PCPartsIreland can be cloned or forked to run locally.

Install dependencies using:

- `pip3 install -r requirements.txt`

Create an `env.py` file at the root level and configure the same environment variables used in Heroku.

```python
# env.py

import os

os.environ.setdefault("AWS_ACCESS_KEY_ID", "user-inserts-own-aws-access-key-id")
os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "user-inserts-own-aws-secret-access-key")
os.environ.setdefault("DATABASE_URL", "user-inserts-own-postgres-database-url")
os.environ.setdefault("EMAIL_HOST_PASS", "user-inserts-own-gmail-host-api-key")
os.environ.setdefault("EMAIL_HOST_USER", "user-inserts-own-gmail-email-address")
os.environ.setdefault("SECRET_KEY", "any-random-secret-key")
os.environ.setdefault("STRIPE_PUBLIC_KEY", "user-inserts-own-stripe-public-key")
os.environ.setdefault("STRIPE_SECRET_KEY", "user-inserts-own-stripe-secret-key")
os.environ.setdefault("STRIPE_WH_SECRET", "user-inserts-own-stripe-webhook-secret")

os.environ.setdefault("DEBUG", "True")
os.environ.setdefault("DEVELOPMENT", "True")

```

To run locally:

- `python3 manage.py runserver`
- Stop with CTRL+C
- `python3 manage.py makemigrations`
- `python3 manage.py migrate`
- `python3 manage.py createsuperuser`
- `python3 manage.py runserver`

To back up models:

- `python3 manage.py dumpdata your-model > your-model.json`
- Do not back up default admin or user data containing confidential information.

### Running Locally

1. Clone the repository:
   git clone https://www.github.com/colmwoods/PCPartsIreland.git

2. Navigate into the project directory:
   cd PCPartsIreland

3. Create and activate a virtual environment:
   python3 -m venv venv
   source venv/bin/activate  (Mac/Linux)
   venv\Scripts\activate     (Windows)

4. Install dependencies:
   pip3 install -r requirements.txt

5. Create an env.py file at root level and configure environment variables.

6. Apply migrations:
   python3 manage.py migrate

7. Create a superuser:
   python3 manage.py createsuperuser

8. Run the development server:
   python3 manage.py runserver

#### Cloning

Clone the repository:

1. Visit [GitHub repository](https://www.github.com/colmwoods/PCPartsIreland)
2. Click the green “Code” button.
3. Copy the HTTPS/SSH/CLI URL.
4. In Terminal:
   - `git clone https://www.github.com/colmwoods/PCPartsIreland.git`

Alternatively, open in Ona (formerly Gitpod):

[![Open in Ona-Gitpod](https://ona.com/run-in-ona.svg)](https://gitpod.io/#https://www.github.com/colmwoods/PCPartsIreland)

#### Forking

To fork the repository:

1. Log into GitHub and navigate to [PCPartsIreland](https://www.github.com/colmwoods/PCPartsIreland)
2. Click the **Fork** button
3. A copy will be created in your GitHub account

### Local VS Deployment

The deployed version reflects the tested local environment. Minor differences may exist in DEBUG configuration and static file handling, but functionality remains consistent.

## Credits

### Content

| Source | Notes |
| --- | --- |
| [Markdown Builder](https://markdown.2bn.dev) | Help generating Markdown files |
| [Chris Beams](https://chris.beams.io/posts/git-commit) | Git commit message guidance |
| [Boutique Ado](https://codeinstitute.net) | Code Institute walkthrough inspiration |
| [Bootstrap](https://getbootstrap.com) | Responsive front-end framework |
| [AWS S3](https://aws.amazon.com/s3) | Static/media storage |
| [Whitenoise](https://whitenoise.readthedocs.io) | Static file service |
| [Stripe](https://docs.stripe.com/payments/elements) | Payment integration |
| [Gmail API](https://developers.google.com/gmail/api/guides) | Email integration |
| [Python Tutor](https://pythontutor.com) | Python assistance |
| [ChatGPT](https://chatgpt.com) | Debugging and documentation refinement |

### Media

| Source | Notes |
| --- | --- |
| [favicon.io](https://favicon.io) | Favicon generation |
| [Boutique Ado](https://codeinstitute.net) | Sample walkthrough assets |
| [Font Awesome](https://fontawesome.com) | Icons used |
| [Pexels](https://images.pexels.com/photos/416160/pexels-photo-416160.jpeg) | Hero image |
| [Wallhere](https://c.wallhere.com/images/9c/c8/da4b4009f070c8e1dfee43d25f99-2318808.jpg!d) | Background wallpaper |
| [Pixabay](https://cdn.pixabay.com/photo/2017/09/04/16/58/passport-2714675_1280.jpg) | Background wallpaper |
| [DALL-E 3](https://openai.com/index/dall-e-3) | AI generated artwork |
| [TinyPNG](https://tinypng.com) | Image compression |
| [CompressPNG](https://compresspng.com) | Image compression (large files) |
| [CloudConvert](https://cloudconvert.com/webp-converter) | WebP conversion |

### Acknowledgements

- I would like to thank my Code Institute mentor, [Tim Nelson](https://www.github.com/TravelTimN), for the support and guidance throughout the development of PCPartsIreland.
- I would like to thank the [Code Institute](https://codeinstitute.net) Tutor Team for their assistance with troubleshooting and debugging various project issues.
- I would like to thank the [Code Institute Slack community](https://code-institute-room.slack.com) and [Code Institute Discord community](https://discord-portal.codeinstitute.net) for the encouragement and moral support during challenging stages of development.
- I would also like to acknowledge the Code Institute **Boutique Ado** walkthrough project, which provided foundational structure and learning guidance that helped shape the development approach for PCPartsIreland.
- I would like to thank my partner for believing in me and supporting my transition into software development.
- I would like to thank my employer for supporting my career development and progression toward becoming a software developer.