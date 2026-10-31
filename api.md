# warp Python API

Complete reference of every operation, grouped by resource. See [the README](./README.md) for usage and configuration.

## Contents

- [`Benefits`](#benefits)
  - [`Benefits HealthPlans`](#benefits-healthplans)
    - [List Health Plans](#list-health-plans)
    - [Get Health Plan](#get-health-plan)
  - [`Benefits RetirementPlans`](#benefits-retirementplans)
    - [List Retirement Plans](#list-retirement-plans)
    - [Create Retirement Plan](#create-retirement-plan)
    - [Get Retirement Plan](#get-retirement-plan)
    - [Update Retirement Plan](#update-retirement-plan)
  - [`Benefits Deductions`](#benefits-deductions)
    - [List Benefit Deductions](#list-benefit-deductions)
    - [Create Benefit Deduction](#create-benefit-deduction)
    - [Get Benefit Deduction](#get-benefit-deduction)
    - [Update Benefit Deduction](#update-benefit-deduction)
- [`Company`](#company)
  - [Get company](#get-company)
- [`CustomFields`](#customfields)
  - [List Fields](#list-fields)
  - [Create Field](#create-field)
  - [Get Field](#get-field)
  - [Update Field](#update-field)
  - [Archive Field](#archive-field)
  - [Create Field Option](#create-field-option)
  - [Update Field Option](#update-field-option)
  - [Delete Unused Field Option](#delete-unused-field-option)
  - [Archive Field Option](#archive-field-option)
  - [List Field Values](#list-field-values)
  - [Set Field Value](#set-field-value)
  - [Clear Field Value](#clear-field-value)
- [`Departments`](#departments)
  - [List Departments](#list-departments)
  - [Create Department](#create-department)
  - [Update Department](#update-department)
- [`I9Verifications`](#i9verifications)
  - [List I-9 verifications](#list-i-9-verifications)
  - [Get I-9 verification](#get-i-9-verification)
- [`BankAccounts`](#bankaccounts)
  - [List bank accounts](#list-bank-accounts)
  - [Get bank account](#get-bank-account)
- [`Levels`](#levels)
  - [List Job Levels](#list-job-levels)
- [`Offers`](#offers)
  - [List Offers](#list-offers)
  - [Create Offer](#create-offer)
  - [Void Offer](#void-offer)
  - [Extend Offer Deadline](#extend-offer-deadline)
  - [Resend Offer](#resend-offer)
- [`PayRates`](#payrates)
  - [List Pay Rates](#list-pay-rates)
  - [Get Pay Rate](#get-pay-rate)
  - [`PayRates Regular`](#payrates-regular)
    - [Create Regular Pay Rate](#create-regular-pay-rate)
    - [Delete Future Regular Pay Rate](#delete-future-regular-pay-rate)
- [`PaySplits`](#paysplits)
  - [List pay splits](#list-pay-splits)
  - [Get pay split](#get-pay-split)
- [`Payroll`](#payroll)
  - [List Payrolls](#list-payrolls)
  - [Get Payroll](#get-payroll)
  - [List Paychecks](#list-paychecks)
  - [Get Paycheck](#get-paycheck)
- [`TimeOff`](#timeoff)
  - [List Time Off Assignments](#list-time-off-assignments)
  - [List Time Off Balances](#list-time-off-balances)
  - [List Time Off Requests](#list-time-off-requests)
  - [`TimeOff Policies`](#timeoff-policies)
    - [List Time Off Policies](#list-time-off-policies)
    - [Get Time Off Policy](#get-time-off-policy)
- [`Workers`](#workers)
  - [Update Worker](#update-worker)
  - [Get Worker](#get-worker)
  - [Delete Worker](#delete-worker)
  - [Reveal Worker SSNs](#reveal-worker-ssns)
  - [List Workers](#list-workers)
  - [Create Employee](#create-employee)
  - [Create Contractor](#create-contractor)
  - [Invite Worker](#invite-worker)
- [`Workplaces`](#workplaces)
  - [List Workplaces](#list-workplaces)
  - [Create Workplace](#create-workplace)
  - [Update Workplace](#update-workplace)

## Setup

```python
import os

from warp_hr import Warp

client = Warp(
    api_key=os.environ.get("WARP_API_KEY"),
)
```

## `Benefits`

### `Benefits HealthPlans`

Health plan reads and retirement plan and payroll benefit deduction management.

#### List Health Plans

List company health plans. Defaults to active plans. A plan whose effectiveEndDate has elapsed is reported and filtered as terminated.

| Direction | Type |
| --- | --- |
| Request | [`HealthPlanListParams`](./src/warp_hr/types/benefits/health_plan_list_params.py) |
| Response | [`HealthPlanListResponse`](./src/warp_hr/types/benefits/health_plan_list_response.py) |

```python
health_plan = client.benefits.health_plans.list(
    limit="limit",
    statuses=["active"],
)
```

#### Get Health Plan

Get a publicly visible company health plan by id.

| Direction | Type |
| --- | --- |
| Response | [`PublicHealthPlan`](./src/warp_hr/types/benefits/public_health_plan.py) |

```python
health_plan = client.benefits.health_plans.get(
    id="chpl_1234",
)
```

### `Benefits RetirementPlans`

Health plan reads and retirement plan and payroll benefit deduction management.

#### List Retirement Plans

List company retirement plans. Defaults to active plans. A plan whose effectiveEndDate has elapsed is reported and filtered as terminated.

| Direction | Type |
| --- | --- |
| Request | [`RetirementPlanListParams`](./src/warp_hr/types/benefits/retirement_plan_list_params.py) |
| Response | [`RetirementPlanListResponse`](./src/warp_hr/types/benefits/retirement_plan_list_response.py) |

```python
retirement_plan = client.benefits.retirement_plans.list(
    limit="limit",
    statuses=["active"],
)
```

#### Create Retirement Plan

Create a retirement plan for a company on the manual retirement channel.

| Direction | Type |
| --- | --- |
| Request | [`RetirementPlanCreateParams`](./src/warp_hr/types/benefits/retirement_plan_create_params.py) |
| Response | [`PublicRetirementPlan1`](./src/warp_hr/types/benefits/public_retirement_plan_1.py) |

```python
retirement_plan = client.benefits.retirement_plans.create(
    type="401k",
    name="x",
    effective_start_date="",
)
```

#### Get Retirement Plan

Get a company retirement plan by id, regardless of status.

| Direction | Type |
| --- | --- |
| Response | [`PublicRetirementPlan`](./src/warp_hr/types/benefits/public_retirement_plan.py) |

```python
retirement_plan = client.benefits.retirement_plans.get(
    id="crpl_1234",
)
```

#### Update Retirement Plan

Update a retirement plan for a company on the manual retirement channel.

| Direction | Type |
| --- | --- |
| Request | [`RetirementPlanUpdateParams`](./src/warp_hr/types/benefits/retirement_plan_update_params.py) |
| Response | [`PublicRetirementPlan`](./src/warp_hr/types/benefits/public_retirement_plan.py) |

```python
retirement_plan = client.benefits.retirement_plans.update(
    id="crpl_1234",
)
```

### `Benefits Deductions`

Health plan reads and retirement plan and payroll benefit deduction management.

#### List Benefit Deductions

List current payroll benefit deductions. Defaults to active deductions. A deduction whose effectiveEndDate has elapsed is reported and filtered as terminated.

| Direction | Type |
| --- | --- |
| Request | [`DeductionListParams`](./src/warp_hr/types/benefits/deduction_list_params.py) |
| Response | [`DeductionListResponse`](./src/warp_hr/types/benefits/deduction_list_response.py) |

```python
deduction = client.benefits.deductions.list(
    limit="limit",
    statuses=["active"],
)
```

#### Create Benefit Deduction

Create a benefit deduction for a worker.

| Direction | Type |
| --- | --- |
| Request | [`DeductionCreateParams`](./src/warp_hr/types/benefits/deduction_create_params.py) |
| Response | [`PublicBenefitDeduction1`](./src/warp_hr/types/benefits/public_benefit_deduction_1.py) |

```python
deduction = client.benefits.deductions.create(
    worker_id="wrk_1234",
    type="medical",
    calculation={
        "type": "fixed_amount",
        "frequency": "monthly",
        "employee_contribution": {"amount": 0, "currency": "USD"},
        "employer_contribution": {"amount": 0, "currency": "USD"},
    },
    effective_start_date="",
)
```

#### Get Benefit Deduction

Get the current version of a company benefit deduction by id.

| Direction | Type |
| --- | --- |
| Response | [`PublicBenefitDeduction`](./src/warp_hr/types/benefits/public_benefit_deduction.py) |

```python
deduction = client.benefits.deductions.get(
    id="pbdg_1234",
)
```

#### Update Benefit Deduction

Update a benefit deduction. The calculation type cannot change.

| Direction | Type |
| --- | --- |
| Request | [`DeductionUpdateParams`](./src/warp_hr/types/benefits/deduction_update_params.py) |
| Response | [`PublicBenefitDeduction`](./src/warp_hr/types/benefits/public_benefit_deduction.py) |

```python
deduction = client.benefits.deductions.update(
    id="pbdg_1234",
)
```

## `Company`

Read basic information about the company associated with your API key.

### Get company

Get the company associated with your API key, including its unmasked EIN. Requires settings read permission or higher. No parameters are required. The response is the company object directly, and unavailable incorporation dates are null.

| Direction | Type |
| --- | --- |
| Response | [`PublicCompany`](./src/warp_hr/types/public_company.py) |

```python
company = client.company.list()
```

## `CustomFields`

Company-defined custom fields for workers. Field definitions are administered with the workers:custom_fields permission; each field belongs to a worker-data category whose read/write grants govern its values.

### List Fields

List the custom worker field definitions your API key can read. Each field belongs to a worker-data category; fields whose category your key cannot read are omitted unless the key holds workers:custom_fields.

| Direction | Type |
| --- | --- |
| Response | [`CustomFieldListResponse`](./src/warp_hr/types/custom_field_list_response.py) |

```python
custom_field = client.custom_fields.list()
```

### Create Field

Create a custom worker field definition. The field type is immutable after creation. Select and multi_select fields can include their initial options. Access to values derives from the field category; requires the workers:custom_fields permission.

| Direction | Type |
| --- | --- |
| Request | [`CustomFieldCreateParams`](./src/warp_hr/types/custom_field_create_params.py) |
| Response | [`CustomFieldCreateResponse`](./src/warp_hr/types/custom_field_create_response.py) |

```python
custom_field = client.custom_fields.create(
    name="x",
    type="text",
    category="info",
)
```

### Get Field

Get a custom worker field definition, including its select options. Archived options may appear on existing worker values but cannot be newly selected.

| Direction | Type |
| --- | --- |
| Response | [`CustomFieldGetResponse`](./src/warp_hr/types/custom_field_get_response.py) |

```python
custom_field = client.custom_fields.get(
    id="cf_1234",
)
```

### Update Field

Update a custom worker field definition. The field type cannot be changed; create a new field instead. Requires the workers:custom_fields permission; changing the category, access level, or input source requires the manage level.

| Direction | Type |
| --- | --- |
| Request | [`CustomFieldUpdateParams`](./src/warp_hr/types/custom_field_update_params.py) |
| Response | [`CustomFieldUpdateResponse`](./src/warp_hr/types/custom_field_update_response.py) |

```python
custom_field = client.custom_fields.update(
    id="cf_1234",
)
```

### Archive Field

Archive a custom worker field. Archived fields keep their existing worker values but cannot receive new ones. Requires the workers:custom_fields permission at the manage level.

| Direction | Type |
| --- | --- |
| Response | [`CustomFieldArchiveResponse`](./src/warp_hr/types/custom_field_archive_response.py) |

```python
custom_field = client.custom_fields.archive(
    id="cf_1234",
)
```

### Create Field Option

Add an option to a select or multi_select custom worker field. The option value should be treated as stable; the label can change. Requires the workers:custom_fields permission.

| Direction | Type |
| --- | --- |
| Request | [`CustomFieldCreateOptionParams`](./src/warp_hr/types/custom_field_create_option_params.py) |
| Response | [`CustomFieldCreateOptionResponse`](./src/warp_hr/types/custom_field_create_option_response.py) |

```python
custom_field = client.custom_fields.create_option(
    id="cf_1234",
    label="x",
    value="x",
)
```

### Update Field Option

Update the label or sort order of a custom worker field option. Options of archived fields cannot be edited. Requires the workers:custom_fields permission.

| Direction | Type |
| --- | --- |
| Request | [`CustomFieldUpdateOptionParams`](./src/warp_hr/types/custom_field_update_option_params.py) |
| Response | [`CustomFieldUpdateOptionResponse`](./src/warp_hr/types/custom_field_update_option_response.py) |

```python
custom_field = client.custom_fields.update_option(
    id="cfo_1234",
)
```

### Delete Unused Field Option

Delete a custom worker field option that is not applied to any worker. Options in use must be archived instead. Requires the workers:custom_fields permission at the manage level.

```python
client.custom_fields.delete_option(
    id="cfo_1234",
)
```

### Archive Field Option

Archive a custom worker field option. Archived options remain on existing worker values but cannot be newly selected. Requires the workers:custom_fields permission at the manage level.

| Direction | Type |
| --- | --- |
| Response | [`CustomFieldArchiveOptionResponse`](./src/warp_hr/types/custom_field_archive_option_response.py) |

```python
custom_field = client.custom_fields.archive_option(
    id="cfo_1234",
)
```

### List Field Values

List custom field values for workers, optionally filtered by worker or field. Values are returned only for fields whose category your API key can read.

| Direction | Type |
| --- | --- |
| Request | [`CustomFieldListValuesParams`](./src/warp_hr/types/custom_field_list_values_params.py) |
| Response | [`CustomFieldListValuesResponse`](./src/warp_hr/types/custom_field_list_values_response.py) |

```python
custom_field = client.custom_fields.list_values()
```

### Set Field Value

Create or replace a worker's value for a custom field. The value shape must match the field type, and your API key must hold write on the field's category.

| Direction | Type |
| --- | --- |
| Request | [`CustomFieldUpsertValueParams`](./src/warp_hr/types/custom_field_upsert_value_params.py) |
| Response | [`CustomFieldUpsertValueResponse`](./src/warp_hr/types/custom_field_upsert_value_response.py) |

```python
custom_field = client.custom_fields.upsert_value(
    worker_id="wrk_1234",
    field_id="cf_1234",
    value={"type": "text", "value": ""},
)
```

### Clear Field Value

Remove a worker's value for a custom field. Your API key must hold write on the field's category.

| Direction | Type |
| --- | --- |
| Request | [`CustomFieldClearValueParams`](./src/warp_hr/types/custom_field_clear_value_params.py) |

```python
client.custom_fields.clear_value(
    worker_id="wrk_1234",
    field_id="cf_1234",
)
```

## `Departments`

Endpoints for department management. Create, list, and update departments within your company.

### List Departments

List all departments for your company.

| Direction | Type |
| --- | --- |
| Request | [`DepartmentListParams`](./src/warp_hr/types/department_list_params.py) |
| Response | [`DepartmentListResponse`](./src/warp_hr/types/department_list_response.py) |

```python
department = client.departments.list(
    limit="limit",
)
```

### Create Department

Create a new department.

| Direction | Type |
| --- | --- |
| Request | [`DepartmentCreateParams`](./src/warp_hr/types/department_create_params.py) |
| Response | [`DepartmentCreateResponse`](./src/warp_hr/types/department_create_response.py) |

```python
department = client.departments.create(
    name="x",
)
```

### Update Department

Update an existing department.

| Direction | Type |
| --- | --- |
| Request | [`DepartmentUpdateParams`](./src/warp_hr/types/department_update_params.py) |
| Response | [`DepartmentUpdateResponse`](./src/warp_hr/types/department_update_response.py) |

```python
department = client.departments.update(
    id="dpt_1234",
)
```

## `I9Verifications`

Read company I-9 verification metadata, including retained forms, without exposing form contents.

### List I-9 verifications

List current and retained company I-9 verifications in all workflow states, newest first. The API key must have workers profile and compliance read scope.

| Direction | Type |
| --- | --- |
| Request | [`I9VerificationListParams`](./src/warp_hr/types/i9_verification_list_params.py) |
| Response | [`I9VerificationListResponse`](./src/warp_hr/types/i9_verification_list_response.py) |

```python
i9_verification = client.i9_verifications.list(
    limit="limit",
)
```

### Get I-9 verification

Get a specific I-9 verification by its id. The API key must have workers profile and compliance read scope.

| Direction | Type |
| --- | --- |
| Response | [`PublicI9Verification`](./src/warp_hr/types/public_i9_verification.py) |

```python
i9_verification = client.i9_verifications.get(
    id="i9v_1234",
)
```

## `BankAccounts`

Read masked worker bank account metadata. No banking instructions or account changes are supported.

### List bank accounts

List stored worker bank accounts, newest first. Requires workers banking and profile read scopes.

| Direction | Type |
| --- | --- |
| Request | [`BankAccountListParams`](./src/warp_hr/types/bank_account_list_params.py) |
| Response | [`BankAccountListResponse`](./src/warp_hr/types/bank_account_list_response.py) |

```python
bank_account = client.bank_accounts.list(
    limit="limit",
)
```

### Get bank account

Get a stored worker bank account. Requires workers banking and profile read scopes.

| Direction | Type |
| --- | --- |
| Response | [`PublicBankAccount`](./src/warp_hr/types/public_bank_account.py) |

```python
bank_account = client.bank_accounts.get(
    id="bank_1234",
)
```

## `Levels`

Endpoints for reading the job-level framework configured for your company.

### List Job Levels

List the active standard job levels available to your company.

| Direction | Type |
| --- | --- |
| Response | [`LevelListResponse`](./src/warp_hr/types/level_list_response.py) |

```python
level = client.levels.list()
```

## `Offers`

Endpoints for managing candidate offers. Create and send offers, list existing offers, and manage their lifecycle.

### List Offers

List the candidate offers for your company.

| Direction | Type |
| --- | --- |
| Request | [`OfferListParams`](./src/warp_hr/types/offer_list_params.py) |
| Response | [`OfferListResponse`](./src/warp_hr/types/offer_list_response.py) |

```python
offer = client.offers.list(
    limit="limit",
)
```

### Create Offer

Create and send a candidate offer. The candidate receives an email with a link to the offer portal.

| Direction | Type |
| --- | --- |
| Request | [`OfferCreateParams`](./src/warp_hr/types/offer_create_params.py) |
| Response | [`OfferCreateResponse`](./src/warp_hr/types/offer_create_response.py) |

```python
offer = client.offers.create(
    candidate={"first_name": "x", "last_name": "x", "email": "john@joinwarp.com"},
    position={"title": "x", "start_date": ""},
    worker_type="employee",
    compensation={"pay_basis": "year", "pay_currency": "USD", "pay_rate": 1},
)
```

### Void Offer

Void a previously sent offer. Only sent offers can be voided.

| Direction | Type |
| --- | --- |
| Request | [`OfferVoidParams`](./src/warp_hr/types/offer_void_params.py) |
| Response | [`OfferVoidResponse`](./src/warp_hr/types/offer_void_response.py) |

```python
offer = client.offers.void(
    id="offr_1234",
    void_reason="candidate_declined",
)
```

### Extend Offer Deadline

Extend the expiration deadline of a sent offer.

| Direction | Type |
| --- | --- |
| Request | [`OfferExtendDeadlineParams`](./src/warp_hr/types/offer_extend_deadline_params.py) |
| Response | [`OfferExtendDeadlineResponse`](./src/warp_hr/types/offer_extend_deadline_response.py) |

```python
offer = client.offers.extend_deadline(
    id="offr_1234",
    expiration_time="",
)
```

### Resend Offer

Resend the offer email to the candidate for a sent offer.

| Direction | Type |
| --- | --- |
| Response | [`OfferResendResponse`](./src/warp_hr/types/offer_resend_response.py) |

```python
offer = client.offers.resend(
    id="offr_1234",
)
```

## `PayRates`

Read worker pay rates and create or delete effective-dated regular pay rates. No public pay-rate update operation is exposed.

### List Pay Rates

List pay rates visible to the API key. Results may be filtered by worker, effective start date, or regular/additional type. US and global worker rates require their corresponding compensation read scopes.

| Direction | Type |
| --- | --- |
| Request | [`PayRateListParams`](./src/warp_hr/types/pay_rate_list_params.py) |
| Response | [`PayRateListResponse`](./src/warp_hr/types/pay_rate_list_response.py) |

```python
pay_rate = client.pay_rates.list(
    limit="limit",
)
```

### Get Pay Rate

Get a specific pay rate by id. The API key must have the compensation read scope corresponding to the worker.

| Direction | Type |
| --- | --- |
| Response | [`PublicPayRate`](./src/warp_hr/types/public_pay_rate.py) |

```python
pay_rate = client.pay_rates.get(
    id="pyr_1234",
)
```

### `PayRates Regular`

Read worker pay rates and create or delete effective-dated regular pay rates. No public pay-rate update operation is exposed.

#### Create Regular Pay Rate

Create an effective-dated regular pay rate for a worker. The API key must have the compensation write scope corresponding to the worker classification. Fixed rates require a nonnegative integer amount in minor currency units, and writes accept only currencies with exactly two ISO 4217 minor-unit digits. Amount is required except for variable pay, and requireHoursSubmission is required for hourly pay. An inactive worker’s rate must start on the worker start date; an active worker’s rate must start on or after that date. An existing future rate blocks creation except for a same-start-date replacement. Currency changes must begin at the current pay-period start, or at the worker start date when the worker is inactive, is a pay-as-you-go contractor, or has a future start date. Variable pay returns a null id and stores no fixed pay-rate row. Replacing a fixed row on the same date emits separate deleted and created webhooks; delivery order is not guaranteed. Creating a fixed rate over variable pay emits only the created webhook because no fixed row existed to delete. There is no pay-rate update event.

| Direction | Type |
| --- | --- |
| Request | [`RegularCreateParams`](./src/warp_hr/types/pay_rates/regular_create_params.py) |
| Response | [`PublicCreateRegularPayRateResponse`](./src/warp_hr/types/pay_rates/public_create_regular_pay_rate_response.py) |

```python
regular = client.pay_rates.regular.create(
    worker_id="wrk_khac8380c2Lm",
    type="salary",
    currency="USD",
    effective_date="",
)
```

#### Delete Future Regular Pay Rate

Delete a regular pay rate or variable-pay boundary identified by worker and effective date. The effective date must be strictly after the current UTC date. The API key must have the compensation write scope corresponding to the worker classification. Deletion reopens the predecessor through the deleted range, including when deleting a variable-pay boundary. There is no public PATCH or PUT pay-rate update operation; replace a same-date rate by creating its replacement.

| Direction | Type |
| --- | --- |
| Request | [`RegularDeleteParams`](./src/warp_hr/types/pay_rates/regular_delete_params.py) |

```python
client.pay_rates.regular.delete(
    worker_id="wrk_khac8380c2Lm",
    effective_date="",
)
```

## `PaySplits`

Read stored pay-split configurations without changing banking instructions or guaranteeing payroll execution.

### List pay splits

List stored pay-split configurations, newest first. Defaults to active. Requires workers banking and profile read scopes plus the applicable US or global compensation read scope.

| Direction | Type |
| --- | --- |
| Request | [`PaySplitListParams`](./src/warp_hr/types/pay_split_list_params.py) |
| Response | [`PaySplitListResponse`](./src/warp_hr/types/pay_split_list_response.py) |

```python
pay_split = client.pay_splits.list(
    limit="limit",
    statuses=["active"],
)
```

### Get pay split

Get a stored pay-split configuration, including retained inactive configurations. Requires workers banking and profile read scopes plus the applicable US or global compensation read scope.

| Direction | Type |
| --- | --- |
| Response | [`PaySplitGetResponse`](./src/warp_hr/types/pay_split_get_response.py) |

```python
pay_split = client.pay_splits.get(
    id="nps_1234",
)
```

## `Payroll`

Read-only payrolls and worker-level payroll calculations. Paycheck endpoints use one consistent resource for every worker type; payment execution is outside this API.

### List Payrolls

List payroll summaries newest first with stable cursor ordering. Every amount in totals is expressed in fundingCurrency, the currency the employer uses to fund the payroll. Line-derived categories are converted and rounded per paycheck before aggregation, while netPay remains provider-authoritative. Payroll type visibility follows the API key permissions. All lifecycle statuses are included unless statuses are provided.

| Direction | Type |
| --- | --- |
| Request | [`PayrollListParams`](./src/warp_hr/types/payroll_list_params.py) |
| Response | [`PublicPayrollList`](./src/warp_hr/types/public_payroll_list.py) |

```python
payroll = client.payroll.list(
    limit="limit",
)
```

### Get Payroll

Get a payroll by id. Every amount in totals is expressed in fundingCurrency, the currency the employer uses to fund the payroll. Line-derived categories are converted and rounded per paycheck before aggregation, while netPay remains provider-authoritative. Missing, foreign, unauthorized, or unavailable payrolls return 404.

| Direction | Type |
| --- | --- |
| Response | [`PublicPayrollDetail`](./src/warp_hr/types/public_payroll_detail.py) |

```python
payroll = client.payroll.get(
    id="pay_1234",
)
```

### List Paychecks

List per-worker paycheck summaries newest first with stable cursor ordering. By default, the response includes every worker type visible to the API key, including US W-2 employees, US 1099 contractors, and global contractors; use workerTypes to narrow the results. Payroll type visibility follows the API key permissions. All lifecycle statuses are included unless statuses are provided.

| Direction | Type |
| --- | --- |
| Request | [`PayrollListPaychecksParams`](./src/warp_hr/types/payroll_list_paychecks_params.py) |
| Response | [`PublicPaycheckList`](./src/warp_hr/types/public_paycheck_list.py) |

```python
payroll = client.payroll.list_paychecks(
    limit="limit",
)
```

### Get Paycheck

Get a paycheck by id. All worker types use the same paycheck schema. Categories that do not apply to a worker are represented by zero-valued totals and empty line-item arrays. For example, a US 1099 contractor with no applicable payroll taxes returns zero `workerTaxes` and `employerTaxes` totals and an empty `taxes` array. Missing, foreign, unauthorized, or unavailable paychecks return 404.

| Direction | Type |
| --- | --- |
| Response | [`PublicPaycheckDetail`](./src/warp_hr/types/public_paycheck_detail.py) |

```python
payroll = client.payroll.get_paycheck(
    id="pyc_1234",
)
```

## `TimeOff`

Endpoints for worker time off management. See time off requests, which workers are assigned to which policies, or worker remaining balances.

### List Time Off Assignments

Time off assignments are mappings between workers and time off policies. Useful for finding out which policies a worker is assigned to, or which workers are assigned to a given policy.

| Direction | Type |
| --- | --- |
| Request | [`TimeOffListAssignmentsParams`](./src/warp_hr/types/time_off_list_assignments_params.py) |
| Response | [`TimeOffListAssignmentsResponse`](./src/warp_hr/types/time_off_list_assignments_response.py) |

```python
time_off = client.time_off.list_assignments(
    limit="limit",
)
```

### List Time Off Balances

Get worker remaining time-off balances.

| Direction | Type |
| --- | --- |
| Request | [`TimeOffListBalancesParams`](./src/warp_hr/types/time_off_list_balances_params.py) |
| Response | [`TimeOffListBalancesResponse`](./src/warp_hr/types/time_off_list_balances_response.py) |

```python
time_off = client.time_off.list_balances(
    limit="limit",
)
```

### List Time Off Requests

Get the time off requests that workers in your company have made.

| Direction | Type |
| --- | --- |
| Request | [`TimeOffListRequestsParams`](./src/warp_hr/types/time_off_list_requests_params.py) |
| Response | [`TimeOffListRequestsResponse`](./src/warp_hr/types/time_off_list_requests_response.py) |

```python
time_off = client.time_off.list_requests(
    limit="limit",
)
```

### `TimeOff Policies`

Endpoints for worker time off management. See time off requests, which workers are assigned to which policies, or worker remaining balances.

#### List Time Off Policies

Get the time off policies for your company

| Direction | Type |
| --- | --- |
| Request | [`PolicyListParams`](./src/warp_hr/types/time_off/policy_list_params.py) |
| Response | [`PolicyListResponse`](./src/warp_hr/types/time_off/policy_list_response.py) |

```python
policy = client.time_off.policies.list(
    limit="limit",
)
```

#### Get Time Off Policy

Get a specific time off policy by id

| Direction | Type |
| --- | --- |
| Response | [`PolicyGetResponse`](./src/warp_hr/types/time_off/policy_get_response.py) |

```python
policy = client.time_off.policies.get(
    id="top_1234",
)
```

## `Workers`

Endpoints for worker management. "Workers" include anyone employed by your company, whether US or international, full-time employees or contractors.

### Update Worker

Update a worker and return the updated worker object. Omitted fields remain unchanged. Requires workers:profile write, plus read access to any referenced department, level, or workplace. See individual fields for update restrictions.

| Direction | Type |
| --- | --- |
| Request | [`WorkerUpdateParams`](./src/warp_hr/types/worker_update_params.py) |
| Response | [`WorkerUpdateResponse`](./src/warp_hr/types/worker_update_response.py) |

```python
worker = client.workers.update(
    id="wrk_1234",
)
```

### Get Worker

Get a specific worker by ID.

| Direction | Type |
| --- | --- |
| Response | [`WorkerGetResponse`](./src/warp_hr/types/worker_get_response.py) |

```python
worker = client.workers.get(
    id="wrk_1234",
)
```

### Delete Worker

Delete a worker. Only workers who have not yet completed onboarding can be deleted. Active workers must be properly offboarded.

```python
client.workers.delete(
    id="wrk_1234",
)
```

### Reveal Worker SSNs

Reveal full Social Security numbers for up to 50 workers. Requires the workers:pii read scope. Results preserve request order and use null when a worker has no SSN on file. The request fails if any worker is not found, emits one audit event per worker, and returns Cache-Control: private, no-store.

| Direction | Type |
| --- | --- |
| Request | [`WorkerRevealSsnParams`](./src/warp_hr/types/worker_reveal_ssn_params.py) |
| Response | [`WorkerRevealSsnResponse`](./src/warp_hr/types/worker_reveal_ssn_response.py) |

```python
worker = client.workers.reveal_ssn(
    worker_ids=["wrk_khac8380c2Lm", "wrk_q7Vm2pR9xK4c"],
)
```

### List Workers

List all workers. Workers include anyone employed by the company, whether US or international, full-time employees or contractors.

| Direction | Type |
| --- | --- |
| Request | [`WorkerListParams`](./src/warp_hr/types/worker_list_params.py) |
| Response | [`WorkerListResponse`](./src/warp_hr/types/worker_list_response.py) |

```python
worker = client.workers.list(
    limit="limit",
)
```

### Create Employee

Create a new US employee. The worker will be created in draft status and must be invited separately via the invite endpoint. If hiring in a state without an existing tax registration, you must specify the stateRegistration field.

| Direction | Type |
| --- | --- |
| Request | [`WorkerCreateEmployeeParams`](./src/warp_hr/types/worker_create_employee_params.py) |
| Response | [`WorkerCreateEmployeeResponse`](./src/warp_hr/types/worker_create_employee_response.py) |

```python
worker = client.workers.create_employee(
    first_name="Jonathan",
    last_name="Galt",
    position="Software Engineer",
    start_date="",
    email="john@joinwarp.com",
    department_id="dpt_1234",
    manager_id="wrk_1234",
    work_location={"type": "office", "workplace_id": "wkp_1234"},
    compensation={"amount": 85000, "per": "hour"},
)
```

### Create Contractor

Create a new contractor. The worker will be created in draft status and must be invited separately via the invite endpoint. For business contractors, the businessName field is required.

| Direction | Type |
| --- | --- |
| Request | [`WorkerCreateContractorParams`](./src/warp_hr/types/worker_create_contractor_params.py) |
| Response | [`WorkerCreateContractorResponse`](./src/warp_hr/types/worker_create_contractor_response.py) |

```python
worker = client.workers.create_contractor(
    entity_type="individual",
    first_name="Melissa",
    last_name="Jones",
    position="Design Consultant",
    start_date="",
    email="john@joinwarp.com",
    department_id="dpt_1234",
    manager_id="wrk_1234",
    work_country="AD",
)
```

### Invite Worker

Send or resend the worker invite so they can accept and complete onboarding to Warp. If the worker has already been invited, the invite will be resent with extended validity.

| Direction | Type |
| --- | --- |
| Response | [`WorkerInviteResponse`](./src/warp_hr/types/worker_invite_response.py) |

```python
worker = client.workers.invite(
    id="wrk_1234",
)
```

## `Workplaces`

Endpoints for workplace management. Create, list, and update workplaces within your company.

### List Workplaces

List all workplaces for your company.

| Direction | Type |
| --- | --- |
| Request | [`WorkplaceListParams`](./src/warp_hr/types/workplace_list_params.py) |
| Response | [`WorkplaceListResponse`](./src/warp_hr/types/workplace_list_response.py) |

```python
workplace = client.workplaces.list(
    limit="limit",
)
```

### Create Workplace

Create a new workplace.

| Direction | Type |
| --- | --- |
| Request | [`WorkplaceCreateParams`](./src/warp_hr/types/workplace_create_params.py) |
| Response | [`WorkplaceCreateResponse`](./src/warp_hr/types/workplace_create_response.py) |

```python
workplace = client.workplaces.create(
    name="x",
    type="remote",
    address={"line1": "x", "city": "", "postal_code": "", "state": "AL", "country": "US"},
)
```

### Update Workplace

Update an existing workplace.

| Direction | Type |
| --- | --- |
| Request | [`WorkplaceUpdateParams`](./src/warp_hr/types/workplace_update_params.py) |
| Response | [`WorkplaceUpdateResponse`](./src/warp_hr/types/workplace_update_response.py) |

```python
workplace = client.workplaces.update(
    id="wkp_1234",
)
```
