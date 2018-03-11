Ansible Role: Diffie-Hellman Parameters
=======================================

Uses OpenSSL to generate strong Diffie-Hellman parameters.

Depending on the system and key size generating this keys can take a very long time.
To speedup key generate use `dhparam_use_dsaparam`.

Role Variables
--------------

| Variable                | Required | Default                                       |
| ----------------------- | -------- | --------------------------------------------- |
| dhparam_size            | no       | 4096                                          |
| dhparam_file            | no       | `/etc/ssl/private/dhparam.pem`                |
| dhparam_update_enabled  | no       | false                                         |
| dhparam_update_interval | no       | `weekly`                                      |
| dhparam_use_dsaparam    | no       | false                                         |   

Examples
--------

### Generate dhparams with 2048 bit once
```yaml
- role: bngsudheer.dhparam
  dhparam_size: 2048
```

### Generate dhparams with auto-update cronjob
```yaml
- role: bngsudheer.dhparam
  dhparam_update_enabled: true
```

### Generate dhparams using dsaparam with auto-update cronjob
```yaml
- role: bngsudheer.dhparam
  dhparam_update_enabled: true
  dhparam_use_dsaparam: true
```


References
----------

- [Weak Diffie-Hellman and the Logjam Attack](https://weakdh.org/)
- [Raymii.org on Forward Secrecy & Diffie Hellman Ephemeral Parameters](https://raymii.org/s/tutorials/Strong_SSL_Security_On_nginx.html#Forward_Secrecy_&_Diffie_Hellman_Ephemeral_Parameters)
