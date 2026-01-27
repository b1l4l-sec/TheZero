# SocialEng - Social Engineering Framework

## Overview

SocialEng is a comprehensive OSINT (Open Source Intelligence) and social engineering toolkit designed for authorized security assessments and penetration testing. This module is part of TheZero v2.0 penetration testing suite.

## Features

### 1. Email Harvesting
Extract email addresses from websites and domains for authorized security testing.

**Capabilities:**
- Web scraping for email extraction
- Multi-source aggregation
- Export results to JSON and TXT formats
- Domain-based targeting

**Usage:**
```
./thezero.py → [3] → [1]
```

### 2. Phone Number Validation
Validate and analyze international phone numbers with detailed information.

**Capabilities:**
- International format validation
- Country code identification
- Carrier detection
- Timezone information
- Multiple format outputs (International, National, E164)

**Usage:**
```
./thezero.py → [3] → [2]
```

### 3. Username Generation
Generate potential username variations from personal information.

**Capabilities:**
- Multiple format patterns
- Birth year integration
- Common number combinations
- Social media username suggestions
- Export to JSON/TXT

**Usage:**
```
./thezero.py → [3] → [3]
```

### 4. Target Profiling
Create comprehensive intelligence profiles for authorized assessments.

**Capabilities:**
- Personal information collection
- Professional details
- Social media profile mapping
- Relationship mapping
- Export to JSON/TXT

**Usage:**
```
./thezero.py → [3] → [4]
```

### 5. Social Media Enumeration
Check username availability and discover profiles across platforms.

**Supported Platforms:**
- GitHub
- Twitter/X
- Instagram
- Facebook
- LinkedIn
- Reddit
- YouTube
- Medium
- Pinterest
- TikTok

**Usage:**
```
./thezero.py → [3] → [5]
```

## Output Directory Structure

```
SocialEng/
├── targets/
│   ├── emails_domain_20260119_143022.json
│   ├── emails_domain_20260119_143022.txt
│   ├── usernames_john_doe_20260119_143022.json
│   ├── usernames_john_doe_20260119_143022.txt
│   ├── profile_john_doe_20260119_143022.json
│   ├── profile_john_doe_20260119_143022.txt
│   ├── social_enum_username_20260119_143022.json
│   └── social_enum_username_20260119_143022.txt
└── modules/
    ├── email_harvester.py
    ├── phone_validator.py
    ├── username_generator.py
    ├── target_profiler.py
    └── social_enum.py
```

## Legal & Ethical Guidelines

### CRITICAL WARNING

This framework is designed **EXCLUSIVELY** for:
- Authorized penetration testing with written permission
- Security assessments with proper authorization
- Educational and research purposes
- CTF competitions and training environments

### PROHIBITED USES

- Unauthorized intelligence gathering
- Social engineering attacks without consent
- Privacy violations
- Harassment or stalking
- Any illegal activity

### Requirements

Before using this framework, you MUST:
1. Obtain written authorization from target organization
2. Ensure compliance with local laws and regulations
3. Follow responsible disclosure practices
4. Respect privacy and data protection laws

**Users are solely responsible for ensuring lawful and authorized use.**

## Dependencies

Required Python packages (installed automatically via Setup.sh):
- `requests` - HTTP requests for web scraping
- `beautifulsoup4` - HTML parsing for email extraction
- `phonenumbers` - International phone number validation
- `lxml` - XML and HTML parsing

## Installation

Dependencies are automatically installed when running:
```bash
./Setup.sh
```

Manual installation:
```bash
pip install requests beautifulsoup4 phonenumbers lxml
```

## Usage Examples

### Example 1: Email Harvesting
```
Target URL: https://example.com
Output: SocialEng/targets/emails_example_com_20260119_143022.json
```

### Example 2: Username Generation
```
Input: First Name: John, Last Name: Doe, Birth Year: 1990
Output: 50+ username variations saved to SocialEng/targets/
```

### Example 3: Social Media Enumeration
```
Input: username123
Output: Found profiles on GitHub, Twitter, LinkedIn
```

## Output Formats

### JSON Format
Structured data with metadata, timestamps, and detailed information.

### TXT Format
Human-readable reports with organized sections and clear formatting.

## Best Practices

1. **Authorization First**: Always obtain proper authorization before gathering intelligence
2. **Document Everything**: Keep records of authorization and scope
3. **Respect Rate Limits**: Avoid aggressive scraping that could impact services
4. **Privacy First**: Handle collected data responsibly and securely
5. **Legal Compliance**: Ensure compliance with GDPR, CCPA, and local laws

## Support

For issues or questions:
- Check the main README.md
- Use option [4] → [3] in TheZero main menu for documentation
- Review QUICKSTART.md for common tasks

## Credits

**Developer**: b1l4l-sec
**GitHub**: https://github.com/b1l4l-sec
**Version**: 2.0
**License**: Educational Use Only

---

**Motto**: *"Every master was once a beginner. Every hero was once a zero."*

**Remember**: With great power comes great responsibility. Use this framework ethically and legally.
