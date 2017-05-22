write-host "Begin Encoding"
$File = $SCRIPT:MyInvocation.MyCommand.Path
$FilePath = split-path $File -parent


$_obj = "init.py",
 	"Debug.py",
	"C_Action.py",
	"C_Bomb.py",
	"C_Troops.py",
	"C_Factories.py",
	"C_Logic.py",
	"C_AI.py",
	"main.py"
$str = ""
$lf = "`r`n"

foreach ($i in $_obj) {
	$_Text = get-content "$FilePath\$($i)" -raw
	$str += $_Text
	$str += "$lf"
}



$str | set-Clipboard
