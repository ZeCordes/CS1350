def create_social_network():
    """Create a sample social network"""
    # Each person maps to their set of friends
    network = {
    'Alice': {'Bob', 'Carol', 'David'},
    'Bob': {'Alice', 'David', 'Eve', 'Frank'},
    'Carol': {'Alice', 'Eve', 'Grace'},
    'David': {'Alice', 'Bob', 'Frank', 'Henry'},
    'Eve': {'Bob', 'Carol', 'Grace', 'Henry'},
    'Frank': {'Bob', 'David', 'Henry', 'Ivy'},
    'Grace': {'Carol', 'Eve', 'Ivy'},
    'Henry': {'David', 'Eve', 'Frank', 'Ivy'},
    'Ivy': {'Frank', 'Grace', 'Henry'}
    }
    return network


def find_mutual_friends(person1: str, person2: str, network: dict[str, set[str]]):
    """
    Find mutual friends between two people.
    Args:
    person1: First person's name
    person2: Second person's name
    network: Social network dictionary
    Returns:
    Set of mutual friends
    """
    friends1 = network[person1]
    friends2 = network[person2]

    return friends1 & friends2


def suggest_friends(person: str, network: dict[str, set[str]], max_suggestions=3):
    """
    Suggest new friends based on mutual connections.
    People with the most mutual friends are suggested first.
    Args:
    person: Person to suggest friends for
    network: Social network dictionary
    max_suggestions: Maximum number of suggestions
    Returns:
    List of (suggested_person, mutual_friend_count) tuples
    """
    # TODO: Find friends of friends who aren't direct friends
    # TODO: Count mutual connections
    # TODO: Return top suggestions
    
    friends = network[person]
    connected = set()
    for friend in friends:
        connected.update(network[friend])
    connected -= friends # remove people who are already friends with the person
    connected.remove(person)
    
    mutuals = []
    for connect_person in connected:
        mutuals.append((connect_person, len(find_mutual_friends(person, connect_person, network))))
    
    mutuals.sort(key=lambda x: x[0])
    
    return mutuals[:max_suggestions] if len(mutuals) >= max_suggestions else mutuals


def find_influencers(network: dict[str, set], min_connections=4):
    """
    Find people with at least min_connections friends.
    Args:
    network: Social network dictionary
    min_connections: Minimum number of connections
    Returns:
    Set of influencer names
    """
    influencers = set()
    for person, friends in network.items():
        if len(friends) >= min_connections:
            influencers.add(person)
    
    return influencers


def test_social_network(network):
    """Test social network analysis"""
    print("\n=== Social Network Analysis ===")
    # Test mutual friends
    mutual = find_mutual_friends('Alice', 'Bob', network)
    print(f"Mutual friends of Alice and Bob: {mutual}")
    # Test friend suggestions
    suggestions = suggest_friends('Alice', network)
    print(f"Friend suggestions for Alice: {suggestions}")
    # Test influencer detection
    influencers = find_influencers(network)
    print(f"Network influencers: {influencers}")


social_network = create_social_network()
# Run tests
test_social_network(social_network)
