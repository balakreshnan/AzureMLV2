import ray
import ray.tune as tune


if __name__ == "__main__":
    ray.init(redis_address = 'localhost:6379')
    
    tune.run("IMPALA",   
             config={
                 "env": "PongNoFrameskip-v4",
                 "num_gpus": 1,
                 "num_workers": 2,
                 "num_envs_per_worker": 5
             },
             local_dir='./logs')
