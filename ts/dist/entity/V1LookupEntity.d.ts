import { FreeMusicEntityBase } from '../FreeMusicEntityBase';
import type { FreeMusicSDK } from '../FreeMusicSDK';
import type { Control } from '../types';
import type { V1Lookup, V1LookupLoadMatch, V1LookupListMatch } from '../FreeMusicTypes';
declare class V1LookupEntity extends FreeMusicEntityBase<V1Lookup> {
    constructor(client: FreeMusicSDK, entopts: any);
    make(this: V1LookupEntity): V1LookupEntity;
    load(this: any, reqmatch?: V1LookupLoadMatch, ctrl?: Control): Promise<V1LookupEntity>;
    list(this: any, reqmatch?: V1LookupListMatch, ctrl?: Control): Promise<V1LookupEntity[]>;
}
export { V1LookupEntity };
