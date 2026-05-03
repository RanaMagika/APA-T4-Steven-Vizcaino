#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Aleat:
    """
    Clase para generar números aleatorios usando el algoritmo LGC.

    >>> rand = Aleat(m=32, a=9, c=13, x0=11)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    16
    29
    18
    15
    >>> rand(29)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    18
    15
    20
    1
    """
    def __init__(self, *, m=2**48, a=25214903917, c=11, x0=1212121):
        """Inicializa los parámetros del generador. El '*' obliga a usar claves."""
        self.m = m
        self.a = a
        self.c = c
        self.x = x0

    def __iter__(self):
        """Un iterador debe devolver el objeto a sí mismo."""
        return self

    def __next__(self):
        """Calcula y devuelve el siguiente número de la secuencia."""
        self.x = (self.a * self.x + self.c) % self.m
        return self.x

    def __call__(self, x0):
        """Reinicia la secuencia con una nueva semilla."""
        self.x = x0


# In[2]:


rand = Aleat(m=32, a=9, c=13, x0=11)
print(next(rand))  # Debería dar 16
print(next(rand))  # Debería dar 29


# In[4]:


def aleat(*, m=2**48, a=25214903917, c=11, x0=1212121):
    """
    Generador de números aleatorios usando el algoritmo LGC.

    >>> rand = aleat(m=64, a=5, c=46, x0=36)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    34
    24
    38
    44
    >>> rand.send(24)
    38
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    44
    10
    32
    14
    """
    x = x0
    while True:
        x = (a * x + c) % m
        
        # yield devuelve x. Si el usuario hace .send(valor), 
        # ese valor se guarda en la variable 'recibido'.
        recibido = yield x
        
        if recibido is not None:
            x = recibido

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)


# In[ ]:




