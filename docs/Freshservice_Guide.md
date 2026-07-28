# Freshservice Issue-Tracking Guide

## Purpose

Freshservice was used to organize and track development work for the Secure Password Generator.

Each planned feature was represented by a Freshservice ticket. Ticket statuses were updated as development progressed.

## Ticket Information

Each ticket includes:

- A clear subject
- A detailed description
- Feature requirements
- Acceptance criteria
- Priority
- Status
- Assignee

## Ticket Workflow

The project uses the following Freshservice workflow:

### Open

The task has been created but development has not started.

### In Progress

Development or testing is currently being completed.

### Resolved

The feature has been implemented, tested, pushed to GitHub, and merged into the `development` branch.

## Development Process

The following process is used for each feature:

1. Create or review the Freshservice ticket.
2. Change the ticket status to `In Progress`.
3. Switch to the appropriate Git feature branch.
4. Merge the latest `development` branch into the feature branch.
5. Implement the required feature.
6. Test the feature.
7. Commit the changes.
8. Push the feature branch to GitHub.
9. Create a pull request into `development`.
10. Review and merge the pull request.
11. Add a resolution note to the Freshservice ticket.
12. Change the ticket status to `Resolved`.

## Connecting Freshservice and GitHub

Freshservice ticket numbers are included in Git commit messages.

Example:

```text
Add password strength assessment - Freshservice #4