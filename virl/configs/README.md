Yes, I'm aware that putting keys and credentials into GitHub is bad practice. These are, however, just labs, and it'll allow people to perfectly reproduce my environment.

Keys generated and exported with:

crypto key gen rsa mod 1024 expor label VIRL 

crypto key export rsa VIRL pem term 3des VIRLVIRL
