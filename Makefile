# Makefile for source rpm: fedora-bookmarks
# $Id$
NAME := fedora-bookmarks
SPECFILE = $(firstword $(wildcard *.spec))

include ../common/Makefile.common
