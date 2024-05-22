import axios from 'axios';
// axios.defaults.baseURL = '';
axios.defaults.baseURL = 'http://127.0.0.1:8002';

// 获取HomeMain中card的内容
export const getCardContent = ({mmd_id,post_time_search_begin,post_time_search_end,rating,sort_by=0,page=0}={}) => 
	axios.get('/api/v1/mmds',{
		params:{
			limit:18,
			offset:18*page,
			mmd_id:mmd_id,
			post_time_search_begin:post_time_search_begin,
			post_time_search_end:post_time_search_end,
			rating:rating,
			sort_by:sort_by
		}
	});
