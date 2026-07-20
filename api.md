# Warp Python API

Complete reference of every operation, grouped by resource. See [the README](./README.md) for usage and configuration.

## Contents

- [`TimeOff`](#timeoff)
  - [List time off assignments](#list-time-off-assignments)
  - [List time off balances](#list-time-off-balances)
  - [List time off requests](#list-time-off-requests)
  - [`TimeOff Policies`](#timeoff-policies)
    - [List time off policies](#list-time-off-policies)
    - [Get time off policy](#get-time-off-policy)
- [`Workers`](#workers)
  - [List workers](#list-workers)
  - [Get worker](#get-worker)
  - [Delete worker](#delete-worker)
  - [Create employee](#create-employee)
  - [Create contractor](#create-contractor)
  - [Invite worker](#invite-worker)
- [`Departments`](#departments)
  - [List departments](#list-departments)
  - [Create department](#create-department)
  - [Update department](#update-department)
- [`Workplaces`](#workplaces)
  - [List workplaces](#list-workplaces)
  - [Create workplace](#create-workplace)
  - [Update workplace](#update-workplace)

## Setup

```python
import os

from warp import Warp

client = Warp(
    api_key=os.environ.get("WARP_API_KEY"),
)
```

## `TimeOff`

### List time off assignments

Time off assignments are mappings between workers and time off policies. Useful for finding out which policies a worker is assigned to, or which workers are assigned to a given policy.

| Direction | Type |
| --- | --- |
| Request | [`TimeOffListAssignmentsParams`](./src/types/time_off_list_assignments_params.py) |
| Response | [`TimeOffListAssignmentsResponse`](./src/types/time_off_list_assignments_response.py) |

```python
time_off = client.time_off.list_assignments()
```

### List time off balances

Get worker remaining time-off balances.

| Direction | Type |
| --- | --- |
| Request | [`TimeOffListBalancesParams`](./src/types/time_off_list_balances_params.py) |
| Response | [`TimeOffListBalancesResponse`](./src/types/time_off_list_balances_response.py) |

```python
time_off = client.time_off.list_balances()
```

### List time off requests

Get the time off requests that workers in your company have made.

| Direction | Type |
| --- | --- |
| Request | [`TimeOffListRequestsParams`](./src/types/time_off_list_requests_params.py) |
| Response | [`TimeOffListRequestsResponse`](./src/types/time_off_list_requests_response.py) |

```python
time_off = client.time_off.list_requests()
```

### `TimeOff Policies`

#### List time off policies

Get the time off policies for your company

| Direction | Type |
| --- | --- |
| Request | [`PolicyListParams`](./src/types/time_off/policy_list_params.py) |
| Response | [`PolicyListResponse`](./src/types/time_off/policy_list_response.py) |

```python
policy = client.time_off.policies.list()
```

#### Get time off policy

Get a specific time off policy by id

| Direction | Type |
| --- | --- |
| Response | [`PolicyRetrieveResponse`](./src/types/time_off/policy_retrieve_response.py) |

```python
policy = client.time_off.policies.retrieve(
    id="top_1234",
)
```

## `Workers`

### List workers

List all workers. Workers include anyone employed by the company, whether US or international, full-time employees or contractors.

| Direction | Type |
| --- | --- |
| Request | [`WorkerListParams`](./src/types/worker_list_params.py) |
| Response | [`WorkerListResponse`](./src/types/worker_list_response.py) |

```python
worker = client.workers.list()
```

### Get worker

Get a specific worker by id.

| Direction | Type |
| --- | --- |
| Response | [`WorkerRetrieveResponse`](./src/types/worker_retrieve_response.py) |

```python
worker = client.workers.retrieve(
    id="wrk_1234",
)
```

### Delete worker

Delete a worker. Only workers who have not yet completed onboarding can be deleted. Active workers must be properly offboarded.

```python
client.workers.delete(
    id="wrk_1234",
)
```

### Create employee

Create a new US employee. The worker will be created in draft status and must be invited separately via the invite endpoint. If hiring in a state without an existing tax registration, you must specify the stateRegistration field.

| Direction | Type |
| --- | --- |
| Request | [`WorkerCreateEmployeeParams`](./src/types/worker_create_employee_params.py) |
| Response | [`WorkerCreateEmployeeResponse`](./src/types/worker_create_employee_response.py) |

```python
worker = client.workers.create_employee(
    first_name="",
    last_name="",
    position="",
    start_date="2000-01-01",
    email="john@joinwarp.com",
    department_id="dpt_1234",
    manager_id="wrk_1234",
    work_location={"type": "office", "workplace_id": "wkp_1234"},
    compensation={"amount": 0, "per": "hour"},
)
```

### Create contractor

Create a new contractor. The worker will be created in draft status and must be invited separately via the invite endpoint. For business contractors, the businessName field is required.

| Direction | Type |
| --- | --- |
| Request | [`WorkerCreateContractorParams`](./src/types/worker_create_contractor_params.py) |
| Response | [`WorkerCreateContractorResponse`](./src/types/worker_create_contractor_response.py) |

```python
worker = client.workers.create_contractor(
    entity_type="individual",
    first_name="",
    last_name="",
    position="",
    start_date="2000-01-01",
    email="john@joinwarp.com",
    department_id="dpt_1234",
    manager_id="wrk_1234",
    work_country="AD",
)
```

### Invite worker

Send or resend the worker invite so they can accept and complete onboarding to Warp. If the worker has already been invited, the invite will be resent with extended validity.

| Direction | Type |
| --- | --- |
| Response | [`WorkerInviteResponse`](./src/types/worker_invite_response.py) |

```python
worker = client.workers.invite(
    id="wrk_1234",
)
```

## `Departments`

### List departments

List all departments for your company.

| Direction | Type |
| --- | --- |
| Request | [`DepartmentListParams`](./src/types/department_list_params.py) |
| Response | [`DepartmentListResponse`](./src/types/department_list_response.py) |

```python
department = client.departments.list()
```

### Create department

Create a new department.

| Direction | Type |
| --- | --- |
| Request | [`DepartmentCreateParams`](./src/types/department_create_params.py) |
| Response | [`DepartmentCreateResponse`](./src/types/department_create_response.py) |

```python
department = client.departments.create(
    name="",
)
```

### Update department

Update an existing department.

| Direction | Type |
| --- | --- |
| Request | [`DepartmentUpdateParams`](./src/types/department_update_params.py) |
| Response | [`DepartmentUpdateResponse`](./src/types/department_update_response.py) |

```python
department = client.departments.update(
    id="dpt_1234",
)
```

## `Workplaces`

### List workplaces

List all workplaces for your company.

| Direction | Type |
| --- | --- |
| Request | [`WorkplaceListParams`](./src/types/workplace_list_params.py) |
| Response | [`WorkplaceListResponse`](./src/types/workplace_list_response.py) |

```python
workplace = client.workplaces.list()
```

### Create workplace

Create a new workplace.

| Direction | Type |
| --- | --- |
| Request | [`WorkplaceCreateParams`](./src/types/workplace_create_params.py) |
| Response | [`WorkplaceCreateResponse`](./src/types/workplace_create_response.py) |

```python
workplace = client.workplaces.create(
    name="",
    type="remote",
    address={"line1": "x", "city": "", "postal_code": "", "state": "AL", "country": "US"},
)
```

### Update workplace

Update an existing workplace.

| Direction | Type |
| --- | --- |
| Request | [`WorkplaceUpdateParams`](./src/types/workplace_update_params.py) |
| Response | [`WorkplaceUpdateResponse`](./src/types/workplace_update_response.py) |

```python
workplace = client.workplaces.update(
    id="wkp_1234",
)
```
