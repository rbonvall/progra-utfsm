CFILES = $(wildcard *.c)
BIN = $(CFILES:.c=)
CC = gcc
CFLAGS = -Wall
LDFLAGS = -lm

all: $(BIN)

%: %.c

clean:
	@rm -v $(BIN)

.PHONY: all clean

