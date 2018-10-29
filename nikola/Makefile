COM_COLOR = \033[0;34m
OBJ_COLOR = \033[0;36m
OK_COLOR = \033[0;32m
ERROR_COLOR = \033[0;31m
WARN_COLOR = \033[0;33m
NO_COLOR = \033[m
ABORT_MSG = \n==========\nAnnulation\n
SUCCESS_MSG = \n========\nSuccès !\n

include .env

deploy:
	@echo -e "\n$(OBJ_COLOR)Construction du site et déploiement sur le serveur"
	@echo -e               "==================================================\n"
	@echo -e "$(COM_COLOR)Reconstruction du site avec Nikola...$(NO_COLOR)"
	@echo "nikola build"; nikola build || (echo -e "\n$(ERROR_COLOR)Erreur : Nikola n'est pas installé dans l'environnement virtuel utilisé.\n$(ABORT_MSG)$(NO_COLOR)"; exit 1)
	@echo -e "$(COM_COLOR)Mise à jour du Mémo Python en PDF...$(NO_COLOR)"
	cp ../../../Programmation/Python/memo/latex/python.pdf output/python.pdf
	@echo -e "$(COM_COLOR)Mise à jour du Mémo Python en RST...$(NO_COLOR)"
	rsync -a --delete ../../../Programmation/Python/memo/rst/_build/html/. output/python/
	@echo -e "$(COM_COLOR)Mise à jour du Mémo OCaml en RST...$(NO_COLOR)"
	rsync -a --delete ../../../Programmation/OCaml/Memo/build/html/. output/ocaml/
	@echo -e "$(WARN_COLOR)"
	@read -p "Transférer le site reconstruit vers $(SITE_PATH) ? Cela va modifier le dossier du site public ! ([O]ui/[N]on) " yn; \
	case $$yn in \
		[OoYy]) \
			(echo -e "\n$(COM_COLOR)Transfert du site reconstruit vers le serveur...$(NO_COLOR)"; echo "rsync -rlPv -e "ssh -p $(SSH_PORT)" --delete output/. $(SSH_USER)@pycolore.fr:$(SITE_PATH)"; rsync -aPv -e "ssh -p $(SSH_PORT)" --delete --info=progress0,stats output/. $(SSH_USER)@pycolore.fr:$(SITE_PATH); echo -e "$(OK_COLOR)\n========\nSuccès !\n$(NO_COLOR)") || (echo -e "\n$(ERROR_COLOR)Erreur : Le transfert des fichiers a échoué.\n$(ABORT_MSG)$(NO_COLOR)"; exit 1);;\
		*) echo -e "$(ERROR_COLOR)$(ABORT_MSG)$(NO_COLOR)" ;;\
	esac

update_docs:
	@echo -e "\n$(OBJ_COLOR)Mise à jour des documents déploiement sur le serveur"
	@echo -e               "====================================================\n"
	@echo -e "$(COM_COLOR)Mise à jour du Mémo Python en PDF...$(NO_COLOR)"
	cp ../../../Programmation/Python/Memo/latex/python.pdf output/python.pdf
	@echo -e "$(COM_COLOR)Mise à jour du Mémo Python en RST...$(NO_COLOR)"
	rsync -a --delete ../../../Programmation/Python/Memo/rst/_build/html/. output/python/
	@echo -e "$(COM_COLOR)Mise à jour du Mémo OCaml en RST...$(NO_COLOR)"
	rsync -a --delete ../../../Programmation/OCaml/Memo/build/html/. output/ocaml/
	@echo -e "$(WARN_COLOR)"
	@read -p "Transférer le site reconstruit vers $(SITE_PATH) ? Cela va modifier le dossier du site public ! ([O]ui/[N]on) " yn; \
	case $$yn in \
		[OoYy]) \
			(echo -e "\n$(COM_COLOR)Transfert du site reconstruit vers le serveur...$(NO_COLOR)"; echo "rsync -rlPv -e "ssh -p $(SSH_PORT)" --delete output/. $(SSH_USER)@pycolore.fr:$(SITE_PATH)"; rsync -aPv -e "ssh -p $(SSH_PORT)" --delete --info=progress0,stats output/. $(SSH_USER)@pycolore.fr:$(SITE_PATH); echo -e "$(OK_COLOR)\n========\nSuccès !\n$(NO_COLOR)") || (echo -e "\n$(ERROR_COLOR)Erreur : Le transfert des fichiers a échoué.\n$(ABORT_MSG)$(NO_COLOR)"; exit 1);;\
		*) echo -e "$(ERROR_COLOR)$(ABORT_MSG)$(NO_COLOR)" ;;\
	esac