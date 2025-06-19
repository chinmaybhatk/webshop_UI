# Webshop UI - Build Fix

## Build Issues Fixed

This branch contains fixes for the following build issues:

### 1. **TypeError: The "path" argument must be of type string. Received undefined**
- **Problem**: The `build.json` file had empty arrays for CSS and JS files, causing esbuild to fail with undefined paths.
- **Solution**: Updated `build.json` to include the actual CSS and JS files:
  ```json
  {
    "css": ["webshop_ui/public/css/organic-theme.css"],
    "js": ["webshop_ui/public/js/organic-theme.js"]
  }
  ```

### 2. **DEPRECATION: Legacy editable install warning**
- **Problem**: The package was using legacy setuptools installation method.
- **Solution**: Added `pyproject.toml` file with modern Python packaging configuration using setuptools>=64.

### 3. **Missing Asset Files**
- **Problem**: The `hooks.py` referenced favicon and splash images that didn't exist.
- **Solution**: Created placeholder files in `webshop_ui/public/images/` directory:
  - `favicon.ico`
  - `splash.png`

### 4. **Package Configuration**
- **Problem**: Basic `package.json` without proper build configuration.
- **Solution**: Enhanced `package.json` with build scripts and Frappe-specific configuration.

### 5. **Hooks Configuration**
- **Problem**: The `hooks.py` file had some configuration issues.
- **Solution**: Cleaned up the hooks file and commented out problematic `user_data_fields` configuration.

## Installation

After these fixes, the app should install properly with:

```bash
bench get-app https://github.com/chinmaybhatk/webshop_UI.git --branch fix-build-issues
bench install-app webshop_ui
```

## Files Modified

- `webshop_ui/public/build.json` - Added CSS and JS file references
- `pyproject.toml` - Added modern Python packaging configuration
- `webshop_ui/public/images/favicon.ico` - Added placeholder favicon
- `webshop_ui/public/images/splash.png` - Added placeholder splash image
- `package.json` - Enhanced with build scripts and Frappe configuration
- `webshop_ui/hooks.py` - Cleaned up configuration

## Next Steps

1. Replace placeholder images with actual favicon and splash images
2. Test the installation in a Frappe environment
3. Add any additional customizations needed for the webshop UI

## Build Process

The build process should now work without the previous errors:
1. Node.js dependencies are installed via yarn
2. esbuild processes the CSS and JS files correctly
3. Python package installs without deprecation warnings
4. All referenced assets are available
