a
    �C=`�  �                   @   s   d dl mZ G dd� d�ZdS )�    )�datec                   @   s8   e Zd ZdZdZdZdd� Zdd� Zdd	� Zd
d� Z	dS )�Pessoau   José�-   gffffff�?c                 C   s   t |� d S �N��print)�selfZtexto� r	   �Bc:\Users\SN00076596.FIEMA\Desktop\Ramon Phyton\POO\aula1\Pessoa.py�falar
   s    zPessoa.falarc                 C   s
   t �  d S r   r   �r   r	   r	   r
   �pensar   s    zPessoa.pensarc                 C   s   d S r   r	   r   r	   r	   r
   �deitar   s    zPessoa.deitarc                 C   s    t �� j}td|| � �� d S )NzVoce nasceu no ano de )r   ZtodayZyearr   )r   �idadeZanoAtualr	   r	   r
   �
calculaAno   s    
zPessoa.calculaAnoN)
�__name__�
__module__�__qualname__ZNomer   Zalturar   r   r   r   r	   r	   r	   r
   r      s   r   N)Zdatetimer   r   r	   r	   r	   r
   �<module>   s   