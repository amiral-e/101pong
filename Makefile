##
## EPITECH PROJECT, 2020
## 101pong
## File description:
## Makefile
##

### SOURCES ###
#----c_sources----#
SRC			:= 101pong.py
### SOURCES ###


### COMPILE_USEFULL ###
#----project_usefull----#
NAME		=	101pong
MAKEFLAGS 	+=	--no-print-directory
### COMPILE_USEFULL ###


### COLORS ###
ccred		= /bin/echo -e "\x1b[1m\x1b[33m\#\#\x1b[31m $1\033[0m"
ccyellow	= /bin/echo -e "\x1b[1m\x1b[33m\#\#\x1b[33m $1\033[0m"
ccend		= /bin/echo -e "\x1b[1m\x1b[33m\#\#\x1b[32m $1\033[0m"
### COLORS ###


#------------------------------------------------------------#
.PHONY:		all
all:		$(NAME)
$(NAME):
			cp $(SRC) $(NAME)
			chmod +x $(NAME)
			@$(call ccend, "Lib successfully compiled.")

#------------------------------------------------------------#
.PHONY:		tests_run
tests_run:	fclean
			@python3 -m unittest discover test/ -v -b
			@$(call ccend, "Unit tests successfully compiled.")

#------------------------------------------------------------#
.PHONY:		clean
clean:
			$(RM) -rf src/__pycache__ test/__pycache__
			@$(call ccyellow, "Lib cleaned.")

#------------------------------------------------------------#
.PHONY:		fclean
fclean:		clean
			$(RM) $(NAME)
			@$(call ccred, "Lib fully cleaned.")

#------------------------------------------------------------#
.PHONY:		re
re:			fclean all