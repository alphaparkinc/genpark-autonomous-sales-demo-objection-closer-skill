from client import AutonomousSalesDemoObjectionCloserClient

def main():
    client = AutonomousSalesDemoObjectionCloserClient()
    inquiry = "We are concerned about data privacy and latency in multi-agent executions."
    res = client.handle_sales_pitch(inquiry)
    print(f"Readiness Score: {res['conversion_readiness_score']}/10")
    print(f"Strategy: {res['objection_response_strategy']}")
    print(f"Demo Pitch: {res['tailored_demo_pitch']}")

if __name__ == "__main__":
    main()
