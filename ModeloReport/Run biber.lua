local arquivo = "Guia_do_modelo"

local command = "biber "..arquivo

local resultado = os.execute(command)

if resultado == 0 then
	print("Conclu�do com sucesso")
else
	print("Conclu�do com erro!")
end

io.read()
