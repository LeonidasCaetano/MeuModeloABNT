local arquivo = "Main"

local command = "lualatex -interaction=nonstopmode -shell-escape "..arquivo..".tex"

local resultado = os.execute(command)

if resultado == 0 then
	print("Conclu�do com sucesso")
	os.execute("start "..arquivo..".pdf")
else
	print("Conclu�do com erro!")
	io.read()
end
