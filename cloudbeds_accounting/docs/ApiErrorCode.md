# ApiErrorCode

Error code indicating the type of failure. Use this value for programmatic error handling. - `UNKNOWN_ERROR` — An unclassified error occurred. Contact support if this persists. - `UNEXPECTED_ERROR` — An unexpected internal error occurred. Retry the request or contact support. - `ACCESS_DENIED` — You do not have permission to perform this operation on the specified property. - `INVALID_REQUEST` — The request body or parameters are invalid. Check the errorDetails field for specifics. - `NOT_UNIQUE_VALUE` — A value that must be unique (such as a name or code) already exists. - `INVALID_USER_INFORMATION` — The user information provided is invalid or could not be resolved. - `ENTITY_NOT_FOUND` — The requested entity was not found. - `ACCOUNTS_RECEIVABLE_LEDGER_FEATURE_DISABLED` — The accounts receivable ledger feature is not enabled for this property. - `BOOKING_NOT_FOUND` — The specified reservation or booking was not found. - `ACCOUNTS_RECEIVABLE_LEDGER_NOT_FOUND` — The specified accounts receivable ledger was not found. - `ACCOUNTS_RECEIVABLE_LEDGER_STATUS_ERROR` — The AR ledger is in a status that does not allow this operation (e.g., attempting to transfer to a closed ledger). - `BOOKING_STATUS_ERROR` — The reservation is in a status that does not allow this operation. - `GROUP_PROFILE_NOT_FOUND` — The specified group profile was not found. - `GROUP_PROFILE_STATUS_ERROR` — The group profile is in a status that does not allow this operation. - `GROUP_PROFILE_FOLIO_ERROR` — An error occurred with the group profile folio (e.g., the specified folio does not belong to the group profile). 

## Enum

* `UNKNOWN_ERROR` (value: `'UNKNOWN_ERROR'`)

* `UNEXPECTED_ERROR` (value: `'UNEXPECTED_ERROR'`)

* `ACCESS_DENIED` (value: `'ACCESS_DENIED'`)

* `INVALID_REQUEST` (value: `'INVALID_REQUEST'`)

* `NOT_UNIQUE_VALUE` (value: `'NOT_UNIQUE_VALUE'`)

* `INVALID_USER_INFORMATION` (value: `'INVALID_USER_INFORMATION'`)

* `ENTITY_NOT_FOUND` (value: `'ENTITY_NOT_FOUND'`)

* `ACCOUNTS_RECEIVABLE_LEDGER_FEATURE_DISABLED` (value: `'ACCOUNTS_RECEIVABLE_LEDGER_FEATURE_DISABLED'`)

* `BOOKING_NOT_FOUND` (value: `'BOOKING_NOT_FOUND'`)

* `ACCOUNTS_RECEIVABLE_LEDGER_NOT_FOUND` (value: `'ACCOUNTS_RECEIVABLE_LEDGER_NOT_FOUND'`)

* `ACCOUNTS_RECEIVABLE_LEDGER_STATUS_ERROR` (value: `'ACCOUNTS_RECEIVABLE_LEDGER_STATUS_ERROR'`)

* `BOOKING_STATUS_ERROR` (value: `'BOOKING_STATUS_ERROR'`)

* `GROUP_PROFILE_NOT_FOUND` (value: `'GROUP_PROFILE_NOT_FOUND'`)

* `GROUP_PROFILE_STATUS_ERROR` (value: `'GROUP_PROFILE_STATUS_ERROR'`)

* `GROUP_PROFILE_FOLIO_ERROR` (value: `'GROUP_PROFILE_FOLIO_ERROR'`)

* `UNKNOWN_DEFAULT_OPEN_API` (value: `'unknown_default_open_api'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


