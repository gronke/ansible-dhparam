Ansible Role: Diffie-Hellman Parameters
=======================================

Uses OpenSSL to generate strong Diffie-Hellman parameters.

Depending on the system and key size generating this keys can take a very long time.

Role Variables
--------------

| Variable     | Required | Default                                       |
| ------------ | -------- | --------------------------------------------- |
| dhparam_size | no       | 4096                                          |
| dhparam_file | no       | `/etc/ssl/certs/dhparam-{{dhparam_size}}.pem` |

Examples
--------

### Generate dhparams with 2048 bit
```yaml
- role: gronke.dhparam
  dhparam_size: 2048
  dhparam_size: /etc/ssl/dhparam.pem
```

References
----------

- [Weak Diffie-Hellman and the Logjam Attack](https://weakdh.org/)
- [Raymii.org on Forward Secrecy & Diffie Hellman Ephemeral Parameters](https://raymii.org/s/tutorials/Strong_SSL_Security_On_nginx.html#Forward_Secrecy_&_Diffie_Hellman_Ephemeral_Parameters)
