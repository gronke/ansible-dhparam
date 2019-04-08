Ansible Role: Diffie-Hellman Parameters
=======================================

Uses OpenSSL to generate strong Diffie-Hellman parameters.

Depending on the system and key size generating this keys can take a very long time.

Role Variables
--------------

| Variable                | Required | Default                                       |
| ----------------------- | -------- | --------------------------------------------- |
| dhparam_size            | no       | 4096                                          |
| dhparam_file            | no       | `/etc/ssl/certs/dhparam-{{dhparam_size}}.pem` |
| dhparam_update_enabled  | no       | false                                         |
| dhparam_update_interval | no       | `weekly`                                      |
| dhparam_entropy_service | no       | false                                         |

Entropy Service
---------------
In virtual machine environements or bare metal hardware that is heavily utilized, generating
high bit-rate cryptographic data sets can deplete the available entropy (random data). This
results in the generation process stalling out while waiting on more entropy to become
available. It is not uncommon on a virtual machine to have as low as a 1024 bit Diffie-Hellman
run take 1-5 minutes and larger bit rates taking considerably longer.

The use of an entropy service, haveged on Debian and rngd on RedHat, resolves this by using the
non-blocking /dev/urandom to supply a constant stream of random data. The consequence of which
is that some of that data may be reused existing entropy, making it suboptimal for long-term
cryotgraphic keys (read: regenerate the data regularly).

As such, on virtual machines or high utilization bare metal systems, it is recommended to enable
the dhparam_entropy_service along with dhparam_update_enabled.

Examples
--------

### Generate dhparams with 2048 bit once
```yaml
- role: gronke.dhparam
  dhparam_size: 2048
  dhparam_file: /etc/ssl/dhparam.pem
```

### Generate dhparams with auto-update cronjob
```yaml
- role: gronke.dhparam
  dhparam_update_enabled: true
```

References
----------

- [Weak Diffie-Hellman and the Logjam Attack](https://weakdh.org/)
- [Raymii.org on Forward Secrecy & Diffie Hellman Ephemeral Parameters](https://raymii.org/s/tutorials/Strong_SSL_Security_On_nginx.html#Forward_Secrecy_&_Diffie_Hellman_Ephemeral_Parameters)
