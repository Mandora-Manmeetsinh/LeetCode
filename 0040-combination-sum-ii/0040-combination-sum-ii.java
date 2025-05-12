class Solution 
{
   public void csum2(int index,List<List<Integer>> ans,List<Integer> list,int[] candidates,int target)
    {
        if(target==0)
        {
            ans.add(new ArrayList<>(list));
            return;
        }
        for(int i=index;i<candidates.length;i++)
        {
            if(i!=index && candidates[i]==candidates[i-1])
            {
                continue;
            }
            if (candidates[i] > target) {
                break; 
            }
            list.add(candidates[i]);
            csum2(i+1,ans,list,candidates,target-candidates[i]);
            list.remove(list.size()-1);
        }
    }

    public List<List<Integer>> combinationSum2(int[] candidates, int target) 
    {
        Arrays.sort(candidates);
        List<List<Integer>> ans=new ArrayList<>();
        List<Integer> list=new ArrayList<>();
        csum2(0,ans,list,candidates,target);
        return ans;       
    }
}