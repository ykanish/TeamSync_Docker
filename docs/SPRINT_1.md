# Sprint 1

## Goal

Implement Workspace Module.

---

## Business Requirement

A user can create one or more workspaces.

Each workspace has:

- Name
- Description
- Logo
- Timezone

---

A workspace can have multiple members.

A member can belong to multiple workspaces.

---

Each workspace can contain channels.

---

Each channel contains messages.

## Workspace Member

A user can belong to multiple workspaces.

A workspace can contain multiple users.

Roles:
- OWNER
- ADMIN
- MEMBER
- GUEST

## Channel

### Business Requirement

A workspace can contain multiple channels.

A channel belongs to exactly one workspace.

Channel types:
- PUBLIC
- PRIVATE

Users can send messages inside channels.

---

### Fields

- workspace
- created_by
- name
- description
- channel_type
- is_active
- created_at
- updated_at

---

### Constraints

A channel name must be unique within a workspace.

Example:

Workspace: TeamSync

✅ general
✅ backend
✅ devops

❌ general
❌ general

However, different workspaces may have the same channel name.

Workspace A:
general

Workspace B:
general

Allowed.

---

### Relationships

Workspace
    |
    | 1
    ▼
Channel

User
    |
    | 1
    ▼
Channel (created_by)

## Message

### Business Requirement

Users can send messages inside channels.

Each message belongs to one channel.

Each message is sent by one user.

Users can edit their own messages.

Users can delete their own messages.

### Relationships

Channel
    |
    | 1
    ▼
Message

User
    |
    | 1
    ▼
Message