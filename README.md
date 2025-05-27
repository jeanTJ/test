# Script Bash : Installation et Configuration Automatisée de Fail2Ban

Ce script Bash permet d’automatiser l’installation, l’activation et la configuration de "Fail2Ban" sur une distribution basée sur "RPM" (comme AlmaLinux, CentOS ou RHEL)**.

#Fonctionnalités

- Vérifie si Fail2Ban est déjà installé
- Installe les paquets nécessaires (`fail2ban`, `fail2ban-firewalld`)
- Crée et configure le fichier `/etc/fail2ban/jail.local`
- Active la protection SSH avec un fichier `sshd.local`
- Relance le service Fail2Ban avec vérification de l'état
- Demande à l’utilisateur les paramètres de bannissement (bantime, findtime, maxretry)

## Prérequis

- Distribution Linux RPM-based
- Privilèges sudo/root
- Pare-feu Firewalld actif
 
