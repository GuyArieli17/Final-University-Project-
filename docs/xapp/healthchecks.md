# Healthchecks

When an RMR healthcheck message arrives, this handler checks that the RMR thread is healthy (if reccive message its healthy).
Healthcheck message can be overwride by by registering a new callback for the healthcheck message type.

----

### Warnings:
- There is no Http service in this framework
- Thre is no generic Healthchecks for General Xapps