### Error 1

[Kaynak](https://stackoverflow.com/questions/56199111/visual-studio-code-cmd-error-cannot-be-loaded-because-running-scripts-is-disabl)

For more simplicity, I want to add the vs code settings path in addition to Ricardo's answer. you can get it like this:

File -> Preferences -> Settings and in the search bar write "automation".

After that, by looking your operating system enter "edit in settings.json".

Finally, add the following b/n the braces:

"terminal.integrated.shellArgs.windows": ["-ExecutionPolicy", "Bypass"]

### Error 2

File C:\Common\Scripts\hello.ps1 cannot be loaded because the execution of scripts is disabled on this system. Please see "get-help about_signing" for more details.
At line:1 char:13
+ .\hello.ps1 <<<<
+ CategoryInfo : NotSpecified: (:) [], PSSecurityException
+ FullyQualifiedErrorId : RuntimeException

[Kaynak2](https://superuser.com/questions/106360/how-to-enable-execution-of-powershell-scripts)
