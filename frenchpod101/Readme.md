# Setup

## Install Selenium package

Run the following command:
```
pip install selenium
```


## Install Gecko driver

1. Go to [Gecko driver GitHub page](https://github.com/mozilla/geckodriver)
2. Download latest Gecko driver binary from releases section
3. Extract binary file into any convenient location, e.g. project directory
4. Update your PATH variable to include binary location:
    1. Copy geckodriver path
    2. Run -> Edit configuration
    3. Add Path to Environment variables

# Troubleshooting

## PATH variable does not contain Gecko driver path

Symptom: `selenium.common.exceptions.WebDriverException: Message: 'geckodriver' executable needs to be in PATH.`

Solution:
- check your PATH variable
- [reinstall Gecko driver](#install-gecko-driver)