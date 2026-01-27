# TheZero Changelog

## Version 2.0 (2026-01-19)

### Major Changes

#### New Module: Social Engineering Framework
- Added comprehensive OSINT toolkit with 5 modules
- Email Harvesting from websites and domains
- Phone Number Validation with international support
- Username Generation with multiple format patterns
- Target Profiling with intelligence aggregation
- Social Media Enumeration across 10+ platforms

#### Branding Updates
- Developer: Changed from "LB Programming" to "b1l4l-sec"
- Removed all Instagram references
- Updated GitHub link to https://github.com/b1l4l-sec
- Version bumped to 2.0 across all modules

#### File Structure Changes
```
NEW DIRECTORIES:
- SocialEng/
- SocialEng/modules/
- SocialEng/targets/

NEW FILES:
- SocialEng/socialeng.py
- SocialEng/modules/__init__.py
- SocialEng/modules/email_harvester.py
- SocialEng/modules/phone_validator.py
- SocialEng/modules/username_generator.py
- SocialEng/modules/target_profiler.py
- SocialEng/modules/social_enum.py
- SocialEng/README.md
- CHANGELOG.md (this file)
```

#### Updated Files
- `thezero.py` - Added SocialEng menu option [3]
- `setup.sh` - Added OSINT dependencies (requests, beautifulsoup4, phonenumbers, lxml)
- `readme.md` - Completely rewritten with new structure
- `quickstart.md` - Added SocialEng quick start guides
- `install.txt` - Updated with v2.0 information
- `Crypto&portScan/logo.py` - Updated branding
- `Crypto&portScan/thezero.py` - Updated exit messages

### Dependencies Added
- `requests` - HTTP requests for web scraping
- `beautifulsoup4` - HTML parsing for email extraction
- `phonenumbers` - International phone validation
- `lxml` - XML and HTML parsing

### Menu Structure Updates

**Main Menu:**
```
[1] Crypto & Port Scanner Suite (Unchanged)
[2] SpecterVision Surveillance (Unchanged)
[3] Social Engineering Framework (NEW)
[4] View Documentation (Previously [3])
[0] Exit
```

**Social Engineering Menu:**
```
[1] Email Harvesting
[2] Phone Number Validation
[3] Username Generation
[4] Target Profiling
[5] Social Media Enumeration
[0] Back to Main Menu
```

### Features Added

#### Email Harvesting
- Web scraping with BeautifulSoup
- Regex-based email extraction
- Multi-source aggregation
- Export to JSON and TXT formats
- Automatic result saving with timestamps

#### Phone Validation
- International format validation
- Country code identification
- Carrier detection
- Timezone information
- Multiple format outputs (International, National, E164)

#### Username Generation
- 50+ username variations from names
- Birth year integration
- Common number combinations
- Social media-friendly formats
- Batch export functionality

#### Target Profiling
- Personal information collection
- Professional details tracking
- Social media profile mapping
- Comprehensive profile exports
- Relationship mapping support

#### Social Media Enumeration
- 10+ platform support (GitHub, Twitter, Instagram, Facebook, LinkedIn, Reddit, YouTube, Medium, Pinterest, TikTok)
- Automated username checking
- Profile discovery
- Availability status tracking
- Detailed reporting

### Documentation Updates
- Complete README.md rewrite
- Enhanced quickstart guide with SocialEng examples
- Updated installation instructions
- Added SocialEng-specific README
- Created comprehensive changelog

### Security & Legal
- Enhanced legal warnings in SocialEng module
- Authorization reminders before operations
- Clear ethical guidelines
- Prohibited uses documentation
- Best practices guide

### Installation Improvements
- Automated dependency installation for OSINT tools
- Directory structure auto-creation
- Enhanced error handling
- Improved setup messaging
- Version display in setup script

---

## Version 1.0 (Previous Release)

### Features
- Crypto & Port Scanner Suite
- SpecterVision Surveillance
- Basic documentation
- Virtual environment support

### Modules
1. Port Scanner (Multi-threaded)
2. Base64/Base32 Encoding
3. Caesar Cipher
4. Password Generator
5. SpecterVision (Camera surveillance with emotion/motion detection)

---

## Migration Guide (1.0 → 2.0)

### For Existing Users:

1. **Backup Data:**
   ```bash
   cp -r SpecterVision/captures ~/backup/captures
   ```

2. **Clean Install:**
   ```bash
   rm -rf venv
   ./Setup.sh
   ```

3. **Launch Updated Version:**
   ```bash
   ./thezero.py
   ```

### New Menu Navigation:
- Old Documentation menu [3] is now [4]
- New SocialEng Framework is [3]

### No Breaking Changes:
- All existing modules (Crypto, SpecterVision) work exactly the same
- Virtual environment management unchanged
- Data storage locations unchanged for existing modules

---

## Roadmap (Future Versions)

### Planned Features:
- Database integration for target data
- Advanced OSINT correlation
- Network mapping visualization
- Automated reporting
- API integrations

### Under Consideration:
- Web-based dashboard
- Multi-threading for OSINT operations
- Custom search engine integration
- Password leak checking

---

**Developer:** b1l4l-sec
**GitHub:** https://github.com/b1l4l-sec
**License:** Educational Use Only

*Last Updated: 2026-01-19*
