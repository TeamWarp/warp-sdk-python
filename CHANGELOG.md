# Changelog

## [0.4.0](https://github.com/TeamWarp/warp-sdk-python/compare/v0.3.0...v0.4.0) (2026-10-31)


### ⚠ BREAKING CHANGES

* **api:** 82 breaking changes to the SDK surface.
    - URL of environment `production` changed from `https://api.joinwarp.com` to `https://api.joinwarp.com/public`.
    - query param `limit` on `departments.list` is now required.
    - `401` error response of `departments.list` changed from `ApiKeyUnauthorized` to `api_key_unauthorized_encoded`.
    - `429` error response of `departments.list` changed from `RateLimitExceeded` to `rate_limit_exceeded_encoded`.
    - `401` error response of `departments.create` changed from `ApiKeyUnauthorized` to `api_key_unauthorized_encoded`.
    - `409` error response of `departments.create` changed from `DepartmentAlreadyExists` to `department_already_exists_encoded`.
    - `429` error response of `departments.create` changed from `RateLimitExceeded` to `rate_limit_exceeded_encoded`.
    - `401` error response of `departments.update` changed from `ApiKeyUnauthorized` to `api_key_unauthorized_encoded`.
    - `404` error response of `departments.update` changed from `DepartmentNotFound` to `department_not_found_encoded`.
    - `409` error response of `departments.update` changed from `DepartmentAlreadyExists` to `department_already_exists_encoded`.
    - `429` error response of `departments.update` changed from `RateLimitExceeded` to `rate_limit_exceeded_encoded`.
    - query param `limit` on `timeOff.listAssignments` is now required.
    - `401` error response of `timeOff.listAssignments` changed from `ApiKeyUnauthorized` to `api_key_unauthorized_encoded`.
    - `429` error response of `timeOff.listAssignments` changed from `RateLimitExceeded` to `rate_limit_exceeded_encoded`.
    - query param `limit` on `timeOff.listBalances` is now required.
    - `401` error response of `timeOff.listBalances` changed from `ApiKeyUnauthorized` to `api_key_unauthorized_encoded`.
    - `404` error response of `timeOff.listBalances` changed from `TimeOffPolicyNotFound` to `time_off_policy_not_found_encoded`.
    - `429` error response of `timeOff.listBalances` changed from `RateLimitExceeded` to `rate_limit_exceeded_encoded`.
    - query param `limit` on `timeOff.listRequests` is now required.
    - `401` error response of `timeOff.listRequests` changed from `ApiKeyUnauthorized` to `api_key_unauthorized_encoded`.
    - `404` error response of `timeOff.listRequests` changed from `TimeOffRequestNotFoundError` to `time_off_request_not_found_error_encoded`.
    - `429` error response of `timeOff.listRequests` changed from `RateLimitExceeded` to `rate_limit_exceeded_encoded`.
    - query param `limit` on `timeOff.policies.list` is now required.
    - `401` error response of `timeOff.policies.list` changed from `ApiKeyUnauthorized` to `api_key_unauthorized_encoded`.
    - `404` error response of `timeOff.policies.list` changed from `TimeOffPolicyNotFound` to `time_off_policy_not_found_encoded`.
    - `429` error response of `timeOff.policies.list` changed from `RateLimitExceeded` to `rate_limit_exceeded_encoded`.
    - `401` error response of `workers.delete` changed from `ApiKeyUnauthorized` to `api_key_unauthorized_encoded`.
    - `404` error response of `workers.delete` changed from `WorkerNotFoundError` to `worker_not_found_error_encoded`.
    - `409` error response of `workers.delete` changed from `CannotDeleteWorker` to `cannot_delete_worker_encoded`.
    - `429` error response of `workers.delete` changed from `RateLimitExceeded` to `rate_limit_exceeded_encoded`.
    - query param `limit` on `workers.list` is now required.
    - `401` error response of `workers.list` changed from `ApiKeyUnauthorized` to `api_key_unauthorized_encoded`.
    - `429` error response of `workers.list` changed from `RateLimitExceeded` to `rate_limit_exceeded_encoded`.
    - `400` error response of `workers.createEmployee` changed from `application/json` to `state_registration_required_encoded`.
    - `401` error response of `workers.createEmployee` changed from `ApiKeyUnauthorized` to `api_key_unauthorized_encoded`.
    - `429` error response of `workers.createEmployee` changed from `RateLimitExceeded` to `rate_limit_exceeded_encoded`.
    - `401` error response of `workers.createContractor` changed from `ApiKeyUnauthorized` to `api_key_unauthorized_encoded`.
    - `429` error response of `workers.createContractor` changed from `RateLimitExceeded` to `rate_limit_exceeded_encoded`.
    - `401` error response of `workers.invite` changed from `ApiKeyUnauthorized` to `api_key_unauthorized_encoded`.
    - `404` error response of `workers.invite` changed from `WorkerNotFoundError` to `worker_not_found_error_encoded`.
    - `429` error response of `workers.invite` changed from `RateLimitExceeded` to `rate_limit_exceeded_encoded`.
    - query param `limit` on `workplaces.list` is now required.
    - `401` error response of `workplaces.list` changed from `ApiKeyUnauthorized` to `api_key_unauthorized_encoded`.
    - `429` error response of `workplaces.list` changed from `RateLimitExceeded` to `rate_limit_exceeded_encoded`.
    - `400` error response of `workplaces.create` changed from `application/json` to `address_invalid_encoded`.
    - `401` error response of `workplaces.create` changed from `ApiKeyUnauthorized` to `api_key_unauthorized_encoded`.
    - `409` error response of `workplaces.create` changed from `WorkplaceAlreadyExists` to `workplace_already_exists_encoded`.
    - `429` error response of `workplaces.create` changed from `RateLimitExceeded` to `rate_limit_exceeded_encoded`.
    - `401` error response of `workplaces.update` changed from `ApiKeyUnauthorized` to `api_key_unauthorized_encoded`.
    - `404` error response of `workplaces.update` changed from `WorkplaceNotFound` to `workplace_not_found_encoded`.
    - `409` error response of `workplaces.update` changed from `WorkplaceAlreadyExists` to `workplace_already_exists_encoded`.
    - `429` error response of `workplaces.update` changed from `RateLimitExceeded` to `rate_limit_exceeded_encoded`.
    - Removed operation `timeOff.policies.retrieve` (`GET /v1/time_off/policies/{id}`).
    - Removed operation `workers.retrieve` (`GET /v1/workers/{id}`).
    - Removed schema `Date`.
    - Removed schema `HttpApiDecodeError`.
    - Removed schema `Issue`.
    - Removed schema `PropertyKey`.
    - Removed schema `InternalServerError`.
    - Removed schema `ApiKeyUnauthorized`.
    - Removed schema `RateLimitExceeded`.
    - Removed schema `DateTimeUtc`.
    - Removed schema `MissingRequiredCompanyPermissions`.
    - Removed schema `ApiNotEnabled`.
    - Removed schema `Trimmed`.
    - Removed schema `DepartmentAlreadyExists`.
    - Removed schema `DepartmentNotFound`.
    - Removed schema `ManagerNotFoundError`.
    - Removed schema `TimeOffPolicyNotFound`.
    - Removed schema `TimeOffRequestNotFoundError`.
    - Removed schema `WorkerNotFoundError`.
    - Removed schema `OfficeWorkLocation`.
    - Removed schema `RemoteWorkLocation`.
    - Removed schema `StateRegistrationRequired`.
    - Removed schema `WorkplaceNotFound`.
    - Removed schema `PayScheduleNotConfigured`.
    - Removed schema `SubscriptionLimitError`.
    - Removed schema `InvalidWorkerStatusError`.
    - Removed schema `WorkerAlreadyExistsError`.
    - Removed schema `CannotDeleteWorker`.
    - Removed schema `AddressInvalid`.
    - Removed schema `WorkplaceAlreadyExists`.
* **api:** Property `MissingRequiredCompanyPermissions.requiredPermissions` type changed from `Array<object>` to `Array<object>`.

### Features

* **api:** initial SDK generation ([8e80652](https://github.com/TeamWarp/warp-sdk-python/commit/8e80652dbfd19bba60028ac25508c60f6c3b9a2c))
* **api:** update environment production (+369 more changes) ([c63939f](https://github.com/TeamWarp/warp-sdk-python/commit/c63939f401df44fb74c2b492a3b45cc5c0b5ffcc))
* **api:** update SDK surface (2 changes) ([56a6df4](https://github.com/TeamWarp/warp-sdk-python/commit/56a6df4ac79da2f80635c2922e1bf6ffa1df4695))


### Chores

* **api:** regenerate SDK ([a5cd83d](https://github.com/TeamWarp/warp-sdk-python/commit/a5cd83dc52e0caed22292ea3555a39f88e1887ce))
* **api:** update generated SDK content ([92d1432](https://github.com/TeamWarp/warp-sdk-python/commit/92d14323f0771d7d328dc80e559cc51124cb69d1))
* initialize SDK repository ([525c5a0](https://github.com/TeamWarp/warp-sdk-python/commit/525c5a0fb87ef6ecce6e7421814b58e51688104d))

## [0.3.0](https://github.com/TeamWarp/warp-sdk-python/compare/v0.2.0...v0.3.0) (2026-10-31)


### ⚠ BREAKING CHANGES

* **api:** 82 breaking changes to the SDK surface.
    - URL of environment `production` changed from `https://api.joinwarp.com` to `https://api.joinwarp.com/public`.
    - query param `limit` on `departments.list` is now required.
    - `401` error response of `departments.list` changed from `ApiKeyUnauthorized` to `api_key_unauthorized_encoded`.
    - `429` error response of `departments.list` changed from `RateLimitExceeded` to `rate_limit_exceeded_encoded`.
    - `401` error response of `departments.create` changed from `ApiKeyUnauthorized` to `api_key_unauthorized_encoded`.
    - `409` error response of `departments.create` changed from `DepartmentAlreadyExists` to `department_already_exists_encoded`.
    - `429` error response of `departments.create` changed from `RateLimitExceeded` to `rate_limit_exceeded_encoded`.
    - `401` error response of `departments.update` changed from `ApiKeyUnauthorized` to `api_key_unauthorized_encoded`.
    - `404` error response of `departments.update` changed from `DepartmentNotFound` to `department_not_found_encoded`.
    - `409` error response of `departments.update` changed from `DepartmentAlreadyExists` to `department_already_exists_encoded`.
    - `429` error response of `departments.update` changed from `RateLimitExceeded` to `rate_limit_exceeded_encoded`.
    - query param `limit` on `timeOff.listAssignments` is now required.
    - `401` error response of `timeOff.listAssignments` changed from `ApiKeyUnauthorized` to `api_key_unauthorized_encoded`.
    - `429` error response of `timeOff.listAssignments` changed from `RateLimitExceeded` to `rate_limit_exceeded_encoded`.
    - query param `limit` on `timeOff.listBalances` is now required.
    - `401` error response of `timeOff.listBalances` changed from `ApiKeyUnauthorized` to `api_key_unauthorized_encoded`.
    - `404` error response of `timeOff.listBalances` changed from `TimeOffPolicyNotFound` to `time_off_policy_not_found_encoded`.
    - `429` error response of `timeOff.listBalances` changed from `RateLimitExceeded` to `rate_limit_exceeded_encoded`.
    - query param `limit` on `timeOff.listRequests` is now required.
    - `401` error response of `timeOff.listRequests` changed from `ApiKeyUnauthorized` to `api_key_unauthorized_encoded`.
    - `404` error response of `timeOff.listRequests` changed from `TimeOffRequestNotFoundError` to `time_off_request_not_found_error_encoded`.
    - `429` error response of `timeOff.listRequests` changed from `RateLimitExceeded` to `rate_limit_exceeded_encoded`.
    - query param `limit` on `timeOff.policies.list` is now required.
    - `401` error response of `timeOff.policies.list` changed from `ApiKeyUnauthorized` to `api_key_unauthorized_encoded`.
    - `404` error response of `timeOff.policies.list` changed from `TimeOffPolicyNotFound` to `time_off_policy_not_found_encoded`.
    - `429` error response of `timeOff.policies.list` changed from `RateLimitExceeded` to `rate_limit_exceeded_encoded`.
    - `401` error response of `workers.delete` changed from `ApiKeyUnauthorized` to `api_key_unauthorized_encoded`.
    - `404` error response of `workers.delete` changed from `WorkerNotFoundError` to `worker_not_found_error_encoded`.
    - `409` error response of `workers.delete` changed from `CannotDeleteWorker` to `cannot_delete_worker_encoded`.
    - `429` error response of `workers.delete` changed from `RateLimitExceeded` to `rate_limit_exceeded_encoded`.
    - query param `limit` on `workers.list` is now required.
    - `401` error response of `workers.list` changed from `ApiKeyUnauthorized` to `api_key_unauthorized_encoded`.
    - `429` error response of `workers.list` changed from `RateLimitExceeded` to `rate_limit_exceeded_encoded`.
    - `400` error response of `workers.createEmployee` changed from `application/json` to `state_registration_required_encoded`.
    - `401` error response of `workers.createEmployee` changed from `ApiKeyUnauthorized` to `api_key_unauthorized_encoded`.
    - `429` error response of `workers.createEmployee` changed from `RateLimitExceeded` to `rate_limit_exceeded_encoded`.
    - `401` error response of `workers.createContractor` changed from `ApiKeyUnauthorized` to `api_key_unauthorized_encoded`.
    - `429` error response of `workers.createContractor` changed from `RateLimitExceeded` to `rate_limit_exceeded_encoded`.
    - `401` error response of `workers.invite` changed from `ApiKeyUnauthorized` to `api_key_unauthorized_encoded`.
    - `404` error response of `workers.invite` changed from `WorkerNotFoundError` to `worker_not_found_error_encoded`.
    - `429` error response of `workers.invite` changed from `RateLimitExceeded` to `rate_limit_exceeded_encoded`.
    - query param `limit` on `workplaces.list` is now required.
    - `401` error response of `workplaces.list` changed from `ApiKeyUnauthorized` to `api_key_unauthorized_encoded`.
    - `429` error response of `workplaces.list` changed from `RateLimitExceeded` to `rate_limit_exceeded_encoded`.
    - `400` error response of `workplaces.create` changed from `application/json` to `address_invalid_encoded`.
    - `401` error response of `workplaces.create` changed from `ApiKeyUnauthorized` to `api_key_unauthorized_encoded`.
    - `409` error response of `workplaces.create` changed from `WorkplaceAlreadyExists` to `workplace_already_exists_encoded`.
    - `429` error response of `workplaces.create` changed from `RateLimitExceeded` to `rate_limit_exceeded_encoded`.
    - `401` error response of `workplaces.update` changed from `ApiKeyUnauthorized` to `api_key_unauthorized_encoded`.
    - `404` error response of `workplaces.update` changed from `WorkplaceNotFound` to `workplace_not_found_encoded`.
    - `409` error response of `workplaces.update` changed from `WorkplaceAlreadyExists` to `workplace_already_exists_encoded`.
    - `429` error response of `workplaces.update` changed from `RateLimitExceeded` to `rate_limit_exceeded_encoded`.
    - Removed operation `timeOff.policies.retrieve` (`GET /v1/time_off/policies/{id}`).
    - Removed operation `workers.retrieve` (`GET /v1/workers/{id}`).
    - Removed schema `Date`.
    - Removed schema `HttpApiDecodeError`.
    - Removed schema `Issue`.
    - Removed schema `PropertyKey`.
    - Removed schema `InternalServerError`.
    - Removed schema `ApiKeyUnauthorized`.
    - Removed schema `RateLimitExceeded`.
    - Removed schema `DateTimeUtc`.
    - Removed schema `MissingRequiredCompanyPermissions`.
    - Removed schema `ApiNotEnabled`.
    - Removed schema `Trimmed`.
    - Removed schema `DepartmentAlreadyExists`.
    - Removed schema `DepartmentNotFound`.
    - Removed schema `ManagerNotFoundError`.
    - Removed schema `TimeOffPolicyNotFound`.
    - Removed schema `TimeOffRequestNotFoundError`.
    - Removed schema `WorkerNotFoundError`.
    - Removed schema `OfficeWorkLocation`.
    - Removed schema `RemoteWorkLocation`.
    - Removed schema `StateRegistrationRequired`.
    - Removed schema `WorkplaceNotFound`.
    - Removed schema `PayScheduleNotConfigured`.
    - Removed schema `SubscriptionLimitError`.
    - Removed schema `InvalidWorkerStatusError`.
    - Removed schema `WorkerAlreadyExistsError`.
    - Removed schema `CannotDeleteWorker`.
    - Removed schema `AddressInvalid`.
    - Removed schema `WorkplaceAlreadyExists`.

### Features

* **api:** update environment production (+369 more changes) ([c63939f](https://github.com/TeamWarp/warp-sdk-python/commit/c63939f401df44fb74c2b492a3b45cc5c0b5ffcc))


### Chores

* **api:** update generated SDK content ([92d1432](https://github.com/TeamWarp/warp-sdk-python/commit/92d14323f0771d7d328dc80e559cc51124cb69d1))

## [0.2.0](https://github.com/TeamWarp/warp-sdk-python/compare/v0.1.0...v0.2.0) (2026-07-21)


### ⚠ BREAKING CHANGES

* **api:** Property `MissingRequiredCompanyPermissions.requiredPermissions` type changed from `Array<object>` to `Array<object>`.

### Features

* **api:** initial SDK generation ([8e80652](https://github.com/TeamWarp/warp-sdk-python/commit/8e80652dbfd19bba60028ac25508c60f6c3b9a2c))
* **api:** update SDK surface (2 changes) ([56a6df4](https://github.com/TeamWarp/warp-sdk-python/commit/56a6df4ac79da2f80635c2922e1bf6ffa1df4695))


### Chores

* **api:** regenerate SDK ([a5cd83d](https://github.com/TeamWarp/warp-sdk-python/commit/a5cd83dc52e0caed22292ea3555a39f88e1887ce))
* initialize SDK repository ([525c5a0](https://github.com/TeamWarp/warp-sdk-python/commit/525c5a0fb87ef6ecce6e7421814b58e51688104d))
