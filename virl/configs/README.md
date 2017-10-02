Yes, I'm aware that putting keys and credentials into GitHub is terrible practice. These are, however, just labs, and it'll allow people to perfectly reproduce my environment. I apologise to those people running scripts trawling GitHub for leaked creds and keys who now have a dozen utterly useless keypairs.

Keys generated and exported with:

crypto key gen rsa mod 1024 expor label VIRL 

crypto key export rsa VIRL pem term 3des VIRLVIRL
