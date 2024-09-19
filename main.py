import hashlib
from multiprocessing import Pool, cpu_count
from tqdm import tqdm

# Paramètres de la difficulté et du nombre de nonces
DIFFICULTY = 6  # Difficulté du minage (nombre de zéros requis en tête du hash)
MAX_TESTED_NONCE = 50000000  # Limite maximale des nonces à tester

# Fonction de hachage SHA-256
def sha256(data):
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

# Fonction qui teste un intervalle de nonces pour trouver un bloc valide
def mine_block_in_range(args):
    block_number, previous_hash, merkle_root, start_nonce, end_nonce = args
    base_text = str(block_number) + merkle_root + previous_hash  # Pré-concaténer la partie statique
    for nonce in range(start_nonce, end_nonce):
        tested_text = base_text + str(nonce) 
        tested_hash = sha256(tested_text)

        # Condition pour trouver un block valide
        if tested_hash[:DIFFICULTY] == '0' * DIFFICULTY:
            return nonce, tested_hash
    
    return None, None

# Fonction principale de minage avec multiprocessing
def mine_block(block_number, previous_hash, merkle_root):
    num_workers = cpu_count()  # Nombre de cœurs CPU
    pool = Pool(num_workers)  # Créer un pool de travailleurs
    step = MAX_TESTED_NONCE // num_workers  # Diviser les nonces à tester

    # Créer des tâches pour chaque cœur
    tasks = [(block_number, previous_hash, merkle_root, i, i + step) for i in range(0, MAX_TESTED_NONCE, step)]

    # Exécuter les tâches en parallèle
    for result in tqdm(pool.imap_unordered(mine_block_in_range, tasks), total=num_workers):
        if result[0] is not None:
            pool.terminate()  # Arrêter tous les autres processus quand une solution est trouvée
            pool.join()       # Assurer la fermeture des processus
            print(f'Block trouvé avec le hash : {result[1]}, et le nonce : {result[0]}')
            return result

    pool.close()  # Fermer le pool après exécution
    pool.join()   # Attendre la fermeture des processus

    return None, None

# Paramètres du bloc
block_number = 1816755767
previous_hash = "00000000000000000000cb1c466ea12f0ee1c5370495e8b8d16138210488f047"
merkle_root = "5c4c35252e6cf35952e86cd64cc5c448092376b87cb5a3f71da56de854c0bd68"

# Lancer le minage
mine_block(block_number, previous_hash, merkle_root)
print("Minage fini!")
