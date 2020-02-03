Local $file = WinWait("[CLASS:#32770]","",10)
ControlSetText($file, "", "Edit1", $CmdLine[1])
Sleep(3000)
ControlClick($file , "", "Button1");