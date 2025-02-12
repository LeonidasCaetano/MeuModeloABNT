local arquivo = "Main"

local command = "lualatex -interaction=nonstopmode -shell-escape "..arquivo..".tex"

local resultado = os.execute(command)

if resultado == 0 then
	print("Concluído com sucesso")
	os.execute("start "..arquivo..".pdf")
else
	print("Concluído com erro!")
	io.read()
end
