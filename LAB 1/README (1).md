# Lab 1 — Requirements Engineering & UML Use-Case Modelling

## Problem Statement #20 — Hospital Bed & ICU Allocation Dashboard

### Problem Overview
The Hospital Bed & ICU Allocation Dashboard is an emergency-room bed management
system that displays real-time ward occupancy, prioritizes ICU transfers based on
a patient's triage score, and orchestrates inter-facility ambulance transfer
workflows when no local ICU bed is available.

### Actors
- **Triage Nurse** — Registers patient vitals, prioritizes patients for ICU bed
  allocation, and initiates inter-facility ambulance transfers when needed.
- **Hospital Administrator** — Monitors ward occupancy, manages bed status
  updates, and coordinates inter-facility ambulance transfers.
- **Ambulance Service** — Receives and handles inter-facility transfer requests
  and dispatches ambulances when no local ICU bed is available.

### Requirements
The requirements specification contains:
- 5 Functional Requirements (FR-001 to FR-005)
- 2 Non-Functional Requirements (NFR-001 to NFR-002)
- Priority, acceptance criteria, and rationale for each requirement.

### Use-Case Diagram
Models all three actors and six use cases (UC-01 to UC-06):
- UC-01 Monitor Ward Occupancy
- UC-02 Register Patient Vitals
- UC-03 Compute Triage Severity Score
- UC-04 Prioritize ICU Bed Allocation
- UC-05 Update Bed Status
- UC-06 Coordinate Ambulance Transfer

Includes the required UML relationships:
- **«include»** — UC-04 (Prioritize ICU Bed Allocation) includes UC-03
  (Compute Triage Severity Score).
- **«extend»** — UC-06 (Coordinate Ambulance Transfer) extends UC-04, under the
  condition *[No local ICU bed available]*.

### Alternate Flow — Activity Diagram
Models the alternate scenario for UC-04 when no suitable local ICU bed is found:
the system displays a message, keeps the patient on the prioritized allocation
list, and routes the case through the Triage Nurse, Hospital Administrator, and
Ambulance Service to complete an inter-facility transfer. The `[YES]` / `[NO]`
decision branches map back to the same «include» (UC-03) and «extend» (UC-06)
relationships shown in the Use-Case Diagram.

### Use-Case Flow
The main documented use case is:

**UC-04 — Prioritize ICU Bed Allocation**

The Use-Case Flow includes:
- Preconditions
- Main Success Scenario
- Alternate Flow
- Postconditions

## Repository Structure
```
LAB1_UTTAM_B_S_PES1UG24CS508/
│
├── README.md
├── Requirements_Table.md
├── Use_Case_Flow.md
│
├── ICU_Dashboard_UseCase_Diagram.pdf
├── ICU_Dashboard_UseCase_Diagram.drawio
├── ICU_Alternate_Flow_Activity_Diagram.pdf
└── ICU_Alternate_Flow_Activity_Diagram.drawio
```
