
function formatar_n_casas(amount,n_casas)
  local formatted = string.gsub(string.format("%."..n_casas.."f",amount),"%.",",")
  while true do
    formatted, k = string.gsub(formatted, "^(-?%d+)(%d%d%d)", '%1.%2')
    if (k==0) then
      break
    end
  end
  return formatted
end
