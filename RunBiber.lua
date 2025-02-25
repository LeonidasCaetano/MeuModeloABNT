local arquivo = "Guia_do_modelo"

local command = "biber "..arquivo

local resultado = os.execute(command)

if resultado == 0 then
	print("Concluído com sucesso")
else
	print("Concluído com erro!")
end

io.read()
