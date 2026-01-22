# User Stories & Agile Planning — PCPartsIreland

This project was planned and managed using an **Agile development methodology**.  
Project requirements were prioritised into **Pass**, **Merit**, and **Distinction** categories, with each category broken down into **User Stories** and smaller implementation **Tasks**.

The complete Agile workflow, including progress tracking and issue management, is available on the GitHub Project Board:  
👉 **[View GitHub Project Board](https://github.com/users/colmwoods/projects/11/views/1)**

---

## Agile Structure

All project functionality was planned and delivered using an **iterative Agile approach**, broken down into three top-level tiers:  
**Pass (LO1–LO6)**, **Merit**, and **Distinction** — each containing detailed **User Stories** and technical **Tasks**.

Every story across all tiers follows the standard Agile format:

> *As a [user type], I want [goal], so that [benefit].*

This ensures all deliverables — from initial features to refinement and polish — remain focused on real user needs and measurable outcomes.

---

## MoSCoW Methodology

This project follows the **MoSCoW prioritisation framework**, mapped directly to Code Institute grading criteria:

- **Must Have → Pass**
- **Should Have → Merit**
- **Could Have → Distinction**

Features identified as *Won’t Have* were reviewed and intentionally excluded from this release where they did not impact core functionality. This demonstrates clear scope control and prioritisation.

---

## Labels & Prioritisation

Each issue and user story in this project is assigned a label based on its priority and Code Institute grading criteria.

| Label | Purpose | Priority |
|------|---------|----------|
| **Pass (Must Have)** | Core functionality required to meet PP5 learning outcomes. | High |
| **Merit (Should Have)** | Refinement features improving usability, documentation, and quality. | Medium |
| **Distinction (Could Have)** | Advanced polish: accessibility, performance, reliability, UX. | Low |

---

## Project Board Columns

| Column | Purpose |
|--------|----------|
| **Todo** | Planned stories awaiting development |
| **In Progress** | Stories actively being built |
| **Done** | Stories completed and meeting acceptance criteria |
| **Merit** | Refinement phase |
| **Distinction** | Advanced polish phase |

---

# PASS — Must Have User Stories (Core)

## P1 — Product Browsing (Catalogue)
> **As a visitor**, I want to browse PC parts by category, so that I can quickly find what I’m looking for.

**Acceptance Criteria:**
- [ ] Product list page exists and loads correctly  
- [ ] Products display key info (name, price, image/placeholder, category)  
- [ ] Category-based filtering is available  

---

## P2 — View Product Details
> **As a visitor**, I want to view a product’s details, so that I can decide whether to purchase it.

**Acceptance Criteria:**
- [ ] Each product has a dedicated detail page  
- [ ] Detail page shows price, description/specifications, and availability  
- [ ] Clear call-to-action exists (add to cart / login to buy)  

---

## P3 — Search Products
> **As a visitor**, I want to search for products, so that I can find specific parts quickly.

**Acceptance Criteria:**
- [ ] Search input is visible and functional  
- [ ] Search results are relevant  
- [ ] No-results message displayed when applicable  

---

## P4 — User Registration
> **As a visitor**, I want to create an account, so that I can purchase products and manage my details.

**Acceptance Criteria:**
- [ ] Registration form works end-to-end  
- [ ] Invalid registrations are prevented  
- [ ] Successful registration provides confirmation  

---

## P5 — Login & Logout
> **As a registered user**, I want to log in and out, so that my account remains secure.

**Acceptance Criteria:**
- [ ] Login accepts valid credentials  
- [ ] Errors shown for invalid credentials  
- [ ] Logout ends the session securely  

---

## P6 — Shopping Cart (Add / Update / Remove)
> **As a user**, I want to manage items in my cart, so that I can control what I’m buying.

**Acceptance Criteria:**
- [ ] Products can be added to cart  
- [ ] Quantities can be updated  
- [ ] Items can be removed  
- [ ] Totals update correctly  

---

## P7 — Checkout / Place Order
> **As a user**, I want to checkout and place an order, so that I can complete my purchase.

**Acceptance Criteria:**
- [ ] Checkout displays order summary  
- [ ] Orders are created and stored successfully  
- [ ] Confirmation message/page is shown  

---

## P8 — Order History
> **As a user**, I want to view my order history, so that I can track previous purchases.

**Acceptance Criteria:**
- [ ] User can view a list of past orders  
- [ ] Orders display date and total  
- [ ] Order detail view is accessible  

---

## P9 — Admin: Product Management
> **As an admin**, I want to manage products, so that the catalogue stays up to date.

**Acceptance Criteria:**
- [ ] Admin can add products  
- [ ] Admin can edit product details  
- [ ] Admin can delete products safely  

---

## P10 — Admin: Order Management
> **As an admin**, I want to manage orders, so that purchases can be fulfilled correctly.

**Acceptance Criteria:**
- [ ] Admin can view all orders  
- [ ] Admin can access order details  
- [ ] Order status can be updated (if implemented)  

---

# MERIT — Should Have User Stories (Refinement)

## M1 — User Feedback Messages
> **As a user**, I want clear success and error messages, so that I understand the result of my actions.

**Acceptance Criteria:**
- [ ] Messages appear for key actions  
- [ ] Styling is consistent  
- [ ] Errors are user-friendly  

---

## M2 — Pagination & Sorting
> **As a visitor**, I want to sort and paginate products, so that browsing is easier.

**Acceptance Criteria:**
- [ ] Pagination implemented where required  
- [ ] Sorting options available  
- [ ] Sorting persists across pages  

---

## M3 — Profile / Address Details
> **As a user**, I want to save delivery details, so that checkout is faster.

**Acceptance Criteria:**
- [ ] Profile page exists  
- [ ] User details can be updated  
- [ ] Checkout can pre-fill saved details (if implemented)  

---

# DISTINCTION — Could Have User Stories (Advanced Polish)

## D1 — Accessibility
> **As a visitor**, I want the site to be accessible, so that all users can interact with it.

**Acceptance Criteria:**
- [ ] Keyboard navigation supported  
- [ ] Form labels implemented correctly  
- [ ] Colour contrast meets accessibility standards  
- [ ] Lighthouse accessibility score ≥ 90  

---

## D2 — Robust Error Handling
> **As a user**, I want clear error handling, so that the site feels reliable.

**Acceptance Criteria:**
- [ ] Custom 404 page  
- [ ] Custom 500 page (where feasible)  
- [ ] Clear validation messaging  

---

## D3 — Performance & UX Polish
> **As a user**, I want fast load times and a clean interface, so that the experience feels professional.

**Acceptance Criteria:**
- [ ] Images optimised  
- [ ] Responsive layout across devices  
- [ ] Consistent spacing and typography  

---

## Tasks (Implementation Notes)

Tasks represent the smallest actionable steps required to implement a User Story, including:
- Model, view, template, and form creation  
- Testing and documentation  
- UX and validation improvements  
- Deployment and configuration  

Each User Story may be linked to GitHub Issues, Pull Requests, or commits.

---

## User Value

Each user story in this document is designed to deliver clear value to users by enabling them to browse, purchase, and manage PC parts efficiently, while providing administrators with full control over products and orders.  
This ensures the application supports a realistic e-commerce workflow aligned with real-world user needs.

---

## Overview

This document outlines all **Pass**, **Merit**, and **Distinction** user stories for **PCPartsIreland**.  
Completion is demonstrated by ticking `[x]` against acceptance criteria, evidencing adherence to Agile planning and delivery principles.

All **Pass** user stories were fully implemented and meet their acceptance criteria.  
Any remaining stories classified as *Won’t Have* were reviewed and intentionally excluded as they did not impact core functionality.