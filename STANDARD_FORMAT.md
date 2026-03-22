# Standard Format Guidelines

## Overview

This document outlines the standard format conventions for commit messages, versioning, and release notes. Following these guidelines ensures consistency across the project, makes the commit history readable, and simplifies maintenance and release management.

## Commit Message Format

#### Structure:

`v.X.Y.Z: [type] <subject>`

### Type Categories

- `[release]`: version release
- `[feat]`: adding new feature
- `[fix]`: bug fix
- `[config]`: configuration file changes
- `[docs]`: documentation changes
- `[refactor]`: code refactoring without feature changes
- `[test]`: adding or updating tests

### Version Format

Follow semantic versioning: `v.MAJOR.MINOR.PATCH`

**Example:**
- `v.1.0.0` - Initial release
- `v.1.1.0` - Minor feature addition
- `v.1.1.1` - Patch/bug fix

## Release Notes Format

#### Structure:

`[v.X.Y.Z] - YYYY-MM-DD`

**Added**

- New features and capabilities

**Changed**

- Changes in existing functionality

**Fixed**

- Bug fixes

**Deprecated**

- Features marked for removal in future versions

**Removed**

- Removed features or functionality

**Security**

- Security fixes and vulnerability patches

**Example:**

```markdown
[v.3.3.0] - 2026-03-22

Added

- Initial release of data-seed-ph
- Core data seeding engine for Philippine data
- Data providers 
- Data exporter for generating seed files
- Comprehensive Philippine-based dataset 
```

