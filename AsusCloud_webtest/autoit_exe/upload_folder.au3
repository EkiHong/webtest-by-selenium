Local $folder = WinWait("[CLASS:#32770]","",10)
ControlSetText($folder, "", "Edit1", $CmdLine[1])
Sleep(3000)
ControlClick($folder , "", "Button1");