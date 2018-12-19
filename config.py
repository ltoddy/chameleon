from ipaddress import ip_address
import socket

__all__ = ['HOST', 'PORT']

HOST = ip_address(socket.INADDR_LOOPBACK).compressed
PORT = 2025
