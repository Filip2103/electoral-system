from models.DB import Db

def get_results_per_states():
    db=Db()
    con=db.get_connection()

    cursor=con.cursor()


    query="""
            SELECT
                s.name,
                cand.name AS candidate_name,
                COUNT(*) AS total_votes,
                ROUND(
                    COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (PARTITION BY s.state_id),
                    2
                ) AS vote_percentage
            FROM votes v
            JOIN candidates cand ON v.candidate_id = cand.candidate_id
            JOIN municipalities m ON v.municipality_id = m.municipality_id
            JOIN cities c ON m.city_id = c.city_id
            JOIN states s ON s.state_id=c.state_id
            GROUP BY s.state_id,s.name, cand.candidate_id, cand.name
            ORDER BY s.name, vote_percentage DESC;
    """

    cursor.execute(query)
    results=cursor.fetchall()
    cursor.close()

    return results

def get_results_per_cities():
    db=Db()
    con=db.get_connection()

    cursor=con.cursor()


    query="""
        SELECT
            c.city_name,
            cand.name AS candidate_name,
            COUNT(*) AS total_votes,
            ROUND(
                COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (PARTITION BY c.city_id),
                2
            ) AS vote_percentage
        FROM votes v
        JOIN candidates cand ON v.candidate_id = cand.candidate_id
        JOIN municipalities m ON v.municipality_id = m.municipality_id
        JOIN cities c ON m.city_id = c.city_id
        GROUP BY c.city_id,c.city_name, cand.candidate_id, cand.name
        ORDER BY c.city_name, vote_percentage DESC;
 
    """

    cursor.execute(query)
    results=cursor.fetchall()
    cursor.close()

    return results

