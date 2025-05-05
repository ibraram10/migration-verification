<h1>Migration Status Checker 3000</h1>
<p>This state of the art script was developed to check the status of websites in a csv file under the Domain column, it automatically lists all 
  the websites that didn't return HTTP status 200</p>
  <h1>How it works? </h1>
  <p>You just provide the csv file, the rows you want to check, and it returns a list of the domains that didn't return HTTP status 200</p>
  <p>and if you are feeling a bit paranoid, it will take screenshots of all the <b>Working</b> websites it visits!

<h1>Usage</h1>

```console
foo@ls:~$  python main.py <file_path> <from_row#> <to_row#>
```

