# Problem Statement

## 1. The "Clean Data" Paradox
Conventional government analytics platforms prioritize clean, standardized datasets. In doing so, they routinely discard "dirty data"—duplicates, null values, and outliers. In the context of Aadhaar enrolment, however, these anomalies are often the primary indicators of systemic friction:
*   **Phantom Enrolments**: High duplicate rejections in a specific locale often indicate fraud rings or poorly trained operators, not just "bad data."
*   **Biometric Failures**: Null returns on biometric updates often signal aging sensor hardware in specific centers.
*   By sanitizing this data before analysis, current systems blindly erase the very operational intelligence required to fix the ground-level issues.

## 2. Retrospective vs. Predictive Infrastructure
Current infrastructure planning relies on decadal census data or static population counts. This leads to a reactive "catch-up" model where Seva Kendras are built only *after* lines have become unmanageable. There is currently no system that uses real-time enrolment velocity to predict where the queue will be six months from now.

## 3. The One-Size-Fits-All Fallacy
Existing allocation logic assigns resources based on simple per-capita ratios (e.g., 1 center per 20,000 people). This fails to account for the *type* of demand:
*   A region with high birth rates needs **Child Enrolment Camps** (portable, home-visit capable).
*   A region with high migration needs **Update Kiosks** (fast, stationary, focus on address/mobile changes).
*   Treating these highly distinct demand profiles as identical "transactions" leads to gross inefficiencies and citizen dissatisfaction.
