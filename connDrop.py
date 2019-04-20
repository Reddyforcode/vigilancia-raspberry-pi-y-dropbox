import dropbox

cliente = dropbox.client.DropboxClient('hfF6VW47cTAAAAAAAAAAD92WnqEw3KHwt4_2b6BDVtXHXY27DfUnkMnTZ7ex-GFL')
print (cliente.account_info)

nombreArchivo ='WHATSAPP.docx'
archivo = open(nombreArchivo, 'rb')
respuesta =cliente.put_file('/DropboxAPI/'+nombreArchivo)

print(respuesta)
