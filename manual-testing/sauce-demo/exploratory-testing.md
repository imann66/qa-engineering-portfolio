# Exploratory Testing Report – Sauce Demo

## 1. Overview

This report documents exploratory testing performed on the Sauce Demo web application.

The objective was to investigate application behavior beyond predefined test cases, focusing on product information, inventory interactions, shopping cart functionality, and checkout.

## 2. Test Environment

| Component    | Details                    |
| ------------ | -------------------------- |
| Application  | Sauce Demo                 |
| URL          | https://www.saucedemo.com/ |
| Browser      | Google Chrome 157.0        |
| Test Account | `problem_user`             |
| Testing Type | Exploratory Testing        |

## 3. Areas Explored

- Product inventory page
- Product images and descriptions
- Add-to-cart functionality
- Shopping cart interactions
- Checkout workflow

## 4. Findings

### Finding 1 – Product Images Do Not Match Product Information

**Observation:**

Some product images displayed did not correspond to their associated product names or descriptions.

**Expected Result:**

Each product should display an image that accurately represents the corresponding product.

**Actual Result:**

Product images were mismatched with product information.

**Impact:**

Users may become confused about which product they are selecting.

### Finding 2 – Product Description Displays Unexpected Code

**Observation:**

A product description displayed the text `carry.allTheThings()` instead of an appropriate product description.

**Expected Result:**

The product description should contain readable and relevant product information.

**Actual Result:**

Unexpected code-like text appeared in the product description.

**Impact:**

The product information is unclear and may reduce user confidence.

### Finding 3 – Add-to-Cart Functionality Was Limited

**Observation:**

During the exploratory session, only three products could be added to the shopping cart.

**Expected Result:**

Products should be addable to the cart according to the application's intended functionality.

**Actual Result:**

Only three products could be added during the recorded session.

**Impact:**

The user may be unable to add other intended products.

**Note:**

This observation is limited to the recorded session. Further testing is required to establish the exact cause and reproducibility.

### Finding 4 – Product Removal Was Unavailable

**Observation:**

The inventory removal functionality was unavailable during the exploratory session.

**Expected Result:**

Users should be able to remove products from the shopping cart when the application provides that functionality.

**Actual Result:**

The expected removal interaction was unavailable during the recorded session.

**Impact:**

Users may have difficulty managing their selected products.

## 5. Defect Tracking

| Finding                           | Status                         |
| --------------------------------- | ------------------------------ |
| Product image mismatch            | Observed                       |
| Unexpected product description    | Observed                       |
| Limited add-to-cart functionality | Requires further investigation |
| Product removal unavailable       | Observed                       |

A separately documented defect, `BUG-001`, covers a checkout issue involving the Last Name and First Name fields.

## 6. Conclusion

Exploratory testing identified multiple unexpected behaviors affecting product information and shopping cart interactions.

The findings demonstrate the value of exploratory testing in discovering issues that may not be covered by predefined test cases.

Further investigation and regression testing would be required to confirm reproducibility and determine the full scope of each finding.

## 7. Limitations

- Testing was performed using the predefined `problem_user` account.
- Findings may be specific to this account.
- Not all observations have been independently reproduced.
- No root cause has been established for the observed issues.
